from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_email_task(subject, message, recipient_list):
    try:
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)

    except Exception as e:
        print(e)
        print('Error sending email!')