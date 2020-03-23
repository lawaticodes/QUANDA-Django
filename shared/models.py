from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=30)
    confirmed = models.BooleanField(default=False)
    logged_in = models.BooleanField(default=False)

    def clean(self):
        if User.objects.filter(email=self.email).count():
            raise ValidationError("An account for this email already exists.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


class Question(models.Model):
    text = models.CharField(max_length=2000)
    datetime = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey("User", related_name="questions", on_delete=models.CASCADE)


class Answer(models.Model):
    question = models.ForeignKey("Question", related_name="answers", on_delete=models.CASCADE)
    text = models.CharField(max_length=2000)
    datetime = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey("User", related_name="answers", on_delete=models.CASCADE)
