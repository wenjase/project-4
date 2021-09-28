from django.db.models.query_utils import Q
from django.shortcuts import render
from .models import User, Question, Answer
# from rest_framework import generics
# from .serializers import UserSerializers, QuestionSerializers, AnswerSerializers
# Create your views here.
#  User views here


# class UserList(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializers

    
# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializers


# class QuestList(generics.ListCreateAPIView):
#     queryset = Question.objects.all()
#     serializer_class = QuestionSerializers

    
    
# class QuestDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Question.objects.all()
#     serializer_class = QuestionSerializers


# class AnswerList(generics.ListCreateAPIView):
#     queryset = Answer.objects.all()
#     serializer_class = AnswerSerializers

# class AnswerDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Answer.objects.all()
#     serializer_class = AnswerSerializers

def user_list(request):
    users = User.objects.all()
    return render(
        request,
        'Q_A/user_list.html',
        {'users': users}
    )

def user_detail(request, pk):
    user = User.objects.get(id=pk)
    return render(
        request,
        'Q_A/user_detail.html',
        {'user': user}
    )

def question_list(request):
    questions = Question.objects.all()
    return render(
        request,
        'Q_A/question_list.html',
        {'questions': questions}
    )

def question_detail(request, pk):
    question = Question.objects.get(id=pk)
    return render(
        request,
        'Q_A/question_detail.html',
        {'question': question}
    )

def answer_list(request):
    answers = Answer.objects.all()
    return render(
        request,
        'Q_A/answer_list.html',
        {'answers': answers}
    )

def answer_detail(request, pk):
    answer = Answer.objects.get(id=pk)
    return render(
        request,
        'Q_A/answer_detail.html',
        {'answer': answer}
    )





