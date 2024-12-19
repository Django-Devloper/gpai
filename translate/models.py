from django.db import models
from accounts.models import  CommonFields
from base.models import Language
from .translate import translate

class Translator(CommonFields):
    input_language = models.ForeignKey(Language , on_delete=models.CASCADE , related_name='input_language')
    output_language = models.ForeignKey(Language , on_delete=models.CASCADE , related_name='output_language')
    user_input = models.TextField()
    assistant_output = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.user_input[:50]

    def save(self, *args, **kwargs):
        if self.user_input:
            self.assistant_output = translate(self.input_language,self.output_language,self.user_input)
        return super().save(*args, **kwargs)
