from django.db import models

from shared.models import Question, Answer


class ForumQuestion(Question):
    pass


class ForumAnswer(Answer):
    chosen = models.BooleanField(default=False)
