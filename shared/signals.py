from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from shared.models import User
from quanda.settings import EMAIL_HOST


@receiver(post_save, sender=User)
def send_confirmation_email(sender, instance, created, **kwargs):
    if created:
        email_message = f"Hi {instance.username}, it's great that you want to be a part of Quanda. Please click " \
                        f"this [INSERT LINK HERE] to complete your registration."

        send_mail("Quanda registration confirmation", email_message, EMAIL_HOST, [instance.email])
