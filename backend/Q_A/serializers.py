from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import User, Question, Answer

class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'password')



class QuestionSerializers(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('id', 'question', 'user')



class AnswerSerializers(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ('id', 'answer', 'question')




