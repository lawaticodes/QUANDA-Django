from django.db import models
from django.utils import timezone


class Question(models.Model):
    text = models.CharField(max_length=2000)
    datetime = models.DateTimeField(default=timezone.now)


class Answer(models.Model):
    question = models.ForeignKey("Question", on_delete=models.CASCADE)
    text = models.CharField(max_length=2000)
    datetime = models.DateTimeField(default=timezone.now)
    chosen = models.BooleanField(default=False)
