from django.core.mail import EmailMessage
from django.db.models.signals import post_save
from django.dispatch import receiver

from shared.models import User
from quanda.settings import EMAIL_HOST
from quanda.urls import MAIN_URL


@receiver(post_save, sender=User)
def send_confirmation_email(sender, instance, created, **kwargs):
    if created:
        confirmation_link = f"{MAIN_URL}/signup/{instance.id}/confirm_user/"
        email_body = f"Hi {instance.username}, it's great that you want to be a part of Quanda.\nPlease click the " \
                     f"following link to complete your registration: {confirmation_link}."
        email = EmailMessage(
            "Quanda registration confirmation",
            email_body,
            EMAIL_HOST,
            [instance.email]
        )
        email.send()
