from rest_framework import permissions, viewsets
from accounts.models import CustomUser
from .models import Translator
from .serializers import TranslatorSerializers
from accounts.serializers import CustomUserSerializers
from translate.translate import queryformater
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response



# Create your views here.

class TranslatorViewSet(viewsets.ModelViewSet):
    queryset = Translator.objects.all()
    serializer_class = TranslatorSerializers
    # permission_classes = [permissions.IsAuthenticated]


class FetchUserViewSet(viewsets.ModelViewSet):
    q = queryformater(CustomUser,"find user with name of admin and email admin@gpai.com")
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializers
    # permission_classes = [permissions.IsAuthenticated]
