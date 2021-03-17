from celery import shared_task
from django.core.mail import send_mail


@shared_task
def sent_message(name, email):
    mail_sent = send_mail("New order", f"new oder from {name} ", 'from@example.com',
                          [email])
    return mail_sent
