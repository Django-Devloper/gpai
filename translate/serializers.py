from rest_framework import serializers
from .models import Translator


class TranslatorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Translator
        fields = ['input_language', 'output_language', 'user_input', 'assistant_output']
