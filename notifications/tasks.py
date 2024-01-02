import json
from celery import shared_task
from datetime import datetime, timedelta
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from notifications.models import IssuedNotification, Notification
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from .consumers import NotificationsConsumer

# @shared_task
# def print_text():
#     print("Hello world")

@shared_task
def todaysnotifications():
    now = datetime.now()
    consumer = NotificationsConsumer()
    print(now)
    notifications_to_send_json = IssuedNotification.objects.filter(
        start_date__lte = now,
        end_date__gte = now,
    )

    truncated_now = now.replace(second=0, microsecond=0)
    now_str = truncated_now.strftime("%H:%M")

    for notification_item in notifications_to_send_json:
        trigger_time_list = list(notification_item.trigger_times.values())
        print(now_str, trigger_time_list)

        if now_str in trigger_time_list:
            print("ALAAAAAAAARRRRM!!!!")
            notification = Notification.objects.get(
                notification_id__exact = notification_item.notification_id 
            )
            msg = {"topic": notification.topic, "body": notification.text}
            print(msg)
            
            hello = send_notification(msg)
            return hello
        else:
            return {"status": "False"}

@shared_task
def send_notification(message):
    channel_layer = get_channel_layer()
    channel_name = "send_notification"
    print("TEST --->", message)
    argo = async_to_sync(channel_layer.group_send)(
        channel_name,
        {
            'type': 'send_notification',
            'message': message,
        }
    
    )
    print(argo)
    