from django.shortcuts import render
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .serializers import UserRegistrationSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = (permissions.AllowAny,)

