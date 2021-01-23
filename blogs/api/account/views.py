from django.contrib.auth import  get_user_model
from rest_framework.permissions import ( AllowAny, IsAuthenciated, IsAuthenticatedOrReadOnly,)
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.genrics import (     CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .serializers import UserSerializer

User = get_user_model()


# Create your views here.
