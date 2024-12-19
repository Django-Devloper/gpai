# myapp/utils/train_model.py

import json
import os
import random
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline, DDIMScheduler
from PIL import Image
from glob import glob
from natsort import natsorted
from django.conf import settings

# Set up paths (you can set them in Django settings.py)
OUTPUT_DIR = settings.BASE_DIR / 'models' / 'stable_diffusion_weights'  # Change according to your desired path
CONCEPTS_LIST_PATH = settings.BASE_DIR / 'models' / 'concepts_list.json'


# Function to train the model
def train_model():
    model_sd = "stable-diffusion-v1-5/stable-diffusion-v1-5"
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    concepts_list = [
        {
            "instance_prompt": "zwx",
            "class_prompt": "photo of a person",
            "instance_data_dir": str(OUTPUT_DIR / "data" / "zwx"),
            "class_data_dir": str(OUTPUT_DIR / "data" / "person"),
        }
    ]

    for c in concepts_list:
        os.makedirs(c["instance_data_dir"], exist_ok=True)

    with open(CONCEPTS_LIST_PATH, "w") as f:
        json.dump(concepts_list, f, indent=4)

    # Additional training hyperparameters
    num_imgs = 10
    num_class_images = num_imgs * 12
    max_num_steps = num_imgs * 80
    learning_rate = 1e-6
    lr_warmup_steps = int(max_num_steps / 10)

    # Execute training script (replacing the shell command)
    os.system(f"""
    python3 train_dreambooth.py \
      --pretrained_model_name_or_path={model_sd} \
      --pretrained_vae_name_or_path="stabilityai/sd-vae-ft-mse" \
      --output_dir={OUTPUT_DIR} \
      --revision="main" \
      --with_prior_preservation --prior_loss_weight=1.0 \
      --seed=777 \
      --resolution=512 \
      --train_batch_size=1 \
      --train_text_encoder \
      --mixed_precision="fp16" \
      --use_8bit_adam \
      --gradient_accumulation_steps=1 \
      --learning_rate={learning_rate} \
      --lr_scheduler="constant" \
      --lr_warmup_steps=80 \
      --num_class_images={num_class_images} \
      --sample_batch_size=4 \
      --max_train_steps={max_num_steps} \
      --save_interval=10000 \
      --save_sample_prompt="zwx" \
      --concepts_list={CONCEPTS_LIST_PATH}
    """)


# Function to generate images using the trained model
def generate_images():
    weights_dir = natsorted(glob(str(OUTPUT_DIR) + os.sep + '*'))[-1]
    ckpt_path = weights_dir + "/model.ckpt"

    pipe = StableDiffusionPipeline.from_pretrained(weights_dir, torch_dtype=torch.float16).to('cuda')
    pipe.scheduler = DDIMScheduler.from_config(pipe.scheduler.config)
    pipe.enable_xformers_memory_efficient_attention()

    # Random seed and prompt
    seed = random.randint(0, 2147483647)
    prompt = "face portrait of zwx in the snow, realistic, hd, vivid, sunset"
    negative_prompt = "bad anatomy, ugly, deformed, distorted face, poorly drawn hands, poorly drawn face, poorly drawn feet, blurry, low quality, low definition, lowres"

    generator = torch.Generator(device='cuda').manual_seed(seed)

    with autocast("cuda"), torch.inference_mode():
        imgs = pipe(
            prompt,
            negative_prompt=negative_prompt,
            height=512, width=512,
            num_images_per_prompt=5,
            num_inference_steps=30,
            guidance_scale=7.5,
            generator=generator
        ).images

    return imgs


# Function to display or save images
def save_images(images):
    # Save images to a directory in Django's static folder
    static_path = settings.STATIC_ROOT / 'generated_images'
    os.makedirs(static_path, exist_ok=True)

    for i, img in enumerate(images):
        img.save(static_path / f"generated_image_{i}.png")

    return static_path
