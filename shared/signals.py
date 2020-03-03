from django.core.mail import EmailMessage
from django.db.models.signals import post_save
from django.dispatch import receiver

from shared.models import User
from quanda.settings import EMAIL_HOST


@receiver(post_save, sender=User)
def send_confirmation_email(sender, instance, created, **kwargs):
    if created:
        EmailMessage(
            "Quanda registration confirmation",
            f"Hi {instance.username}, it's great that you want to be a part of Quanda.\nPlease click "
            f"[INSERT LINK HERE] to complete your registration.",
            EMAIL_HOST,
            [instance.email]
        ).send()
