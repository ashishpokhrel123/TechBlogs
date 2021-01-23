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




# Create your views here.
User = get_user_model()

class UserCreateApiView(CreateAPIView):
    # Create User instance and return username, email 
    #method = Post
    permissions = [AllowAny]
    serializers = [UserSerializer]
class UserListApiView(ListAPIView):
    #return all existing user 
    # method = Get

    queryset = User.objects.all()
    permissions = [IsAuthenciated]
    serializers = [UserSerializer]

