import random
from celery import Celery
from celery import task, shared_task
from django.conf import settings
from django.core.mail import send_mail
from .models import People, WishesText
from datetime import date, datetime

@shared_task(name='send_wishes')
def send_wishes():
    person_data=People.objects.filter(dob__month=date.today().month,dob__day=date.today().day)
    for person in person_data:
        message_obj=WishesText.objects.filter(category=person.category).order_by('time_sent').first()
        
        message_body=message_obj.text

        subject = 'Happy Birthday'
        message = f'Happy Birthday {person.name}, \n{message_body}'
        print(message,end='\n\n')
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [person.email]
        send_mail( subject, message, email_from, recipient_list)
        message_obj.time_sent+=1
        message_obj.save()