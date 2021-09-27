from django.shortcuts import render
from .models import User, Question, Answer
from rest_framework import generics
from .serializers import UserSerializers, QuestionSerializers, AnswerSerializers
# Create your views here.
#  User views here


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

    
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class QuestList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializers

    
    
class QuestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializers


class AnswerList(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializers

class AnswerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializers

