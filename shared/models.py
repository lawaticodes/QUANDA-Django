from django.db import models
from django.utils import timezone


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=30)


class Question(models.Model):
    text = models.CharField(max_length=2000)
    datetime = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey("User", related_name="questions", on_delete=models.CASCADE)


class Answer(models.Model):
    question = models.ForeignKey("Question", related_name="answers", on_delete=models.CASCADE)
    text = models.CharField(max_length=2000)
    datetime = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey("User", related_name="answers", on_delete=models.CASCADE)
