from django.db import models
from django.utils import timezone

from shared.models import Question, Answer


class BundleQuestion(Question):
    pass


class BundleAnswer(Answer):
    pass


class PackageUnit(models.Model):
    package = models.ForeignKey("Package", related_name="package_units", on_delete=models.CASCADE)
    question = models.ForeignKey("BundleQuestion", related_name="package_units", on_delete=models.PROTECT)
    answer = models.ForeignKey("BundleAnswer", related_name="package_units", on_delete=models.PROTECT)


class Package(models.Model):
    sender = models.ForeignKey("shared.User", related_name="sender_packages", on_delete=models.CASCADE)
    receiver = models.ForeignKey("shared.User", related_name="receiver_packages", on_delete=models.PROTECT)
    sent_datetime = models.DateTimeField(default=timezone.now)
