# from django.db import models
# from django.db.models import fields
# from rest_framework import serializers
# from .models import User, Question, Answer

# class UserSerializers(serializers.ModelSerializer):

#     user = serializers.HyperlinkedRelatedField(
#         view_name='user_detail',
#         many=True,
#         read_only=True
#     )

#     class Meta:
#         model = User
#         fields = ('id', 'username', 'password', 'user')



# class QuestionSerializers(serializers.HyperlinkedModelSerializer):
#     questions = serializers.HyperlinkedRelatedField(
#         view_name='question_detail',
#         many=True,
#         read_only=True
#     )

#     class Meta:
#         model = Question
#         fields = ('id', 'question', 'questions')



# class AnswerSerializers(serializers.HyperlinkedModelSerializer):
#     answers = serializers.HyperlinkedRelatedField(
#         view_name='answer_detail',
#         many=True,
#         read_only=True
#     )

#     class Meta:
#         model = Answer
#         fields = ('id', 'answers', 'answer')




