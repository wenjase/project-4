from django.urls import path
from . import views


urlpatterns = [
    # path('users/', views.user_list, name='user_list'),
    # path('users/<int:pk>', views.user_detail, name='user_detail'),
    # path('questions/', views.question_list, name='question_list'),
    # path('questions/<int:pk>', views.question_detail, name='question_detail'),
    # path('answers/', views.answer_list, name='answer_list'),
    # path('answers/<int:pk>', views.answer_detail, name='answer_detail')
    path('users/', views.UserList.as_view(), name='user_list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('questions/', views.QuestList.as_view(), name='question_list'),
    path('question/<int:pk>', views.QuestDetail.as_view(), name='question_detail'),
    path('answers/', views.AnswerList.as_view(), name='answer_list'),
    path('answer/<int:pk>', views.AnswerDetail.as_view(), name='answer_detail')
]