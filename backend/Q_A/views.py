from django.shortcuts import render
from .models import User, Question, Answer
from rest_framework import generics
from .serializers import UserSerializer
# Create your views here.
#  User views here


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


