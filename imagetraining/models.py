from django.db import models
from accounts.models import CommonFields
import os
# Create your models here.

class ObjectModelTraining(CommonFields):
    name = models.CharField(max_length=100)
    seed = models.PositiveIntegerField()
    training_end = models.DateTimeField(null=True,blank=True)
    duration = models.TimeField(null=True,blank=True)
    def __str__(self):
        return self.name

class TrainingImages(models.Model):
    object_model = models.ForeignKey(ObjectModelTraining , on_delete=models.CASCADE)
    file = models.ImageField(upload_to='media/training_image')
    name = models.CharField(max_length=30,null=True,blank=True)
    def __str__(self):
        return self.name

    def save(self ,*args ,**kwargs):
        if self.file and not self.name:
            self.name = os.path.splitext(self.file.name)[0]
        super(TrainingImages, self).save(*args, **kwargs)

class SampleImages(models.Model):
    object_model = models.ForeignKey(ObjectModelTraining , on_delete=models.CASCADE)
    file = models.ImageField(upload_to='media/sample')
    name = models.CharField(max_length=30,null=True,blank=True)

    def __str__(self):
        return self.name