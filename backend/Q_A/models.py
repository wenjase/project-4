from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=15)
    
    def __str__(self):
        return str(self.username)



class Question(models.Model):
    # user = models.ForeignKey(
    #     User,
    #     on_delete=models.CASCADE,
    #     related_name='question'
    # )
    question = models.TextField(max_length=1000)

    def __str__(self):
        return self.question



class Answer(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='answer'
    )
    answer = models.TextField(max_length=1000)

    def __str__(self):
        return self.answer



