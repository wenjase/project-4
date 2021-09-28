from django.urls import path
from . import views


urlpatterns = [
    path('users/', views.user_list, name='user_list'),
    path('users/<int:pk>', views.user_detail, name='user_detail'),
    path('questions/', views.question_list, name='question_list'),
    path('questions/<int:pk>', views.question_detail, name='question_detail'),
    path('answers/', views.answer_list, name='answer_list'),
    path('answers/<int:pk>', views.answer_detail, name='answer_detail')
]