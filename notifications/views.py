from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, authentication_classes, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.shortcuts import get_object_or_404
from notifications.serializer import IssuedNotificationSerializer, NotificationSerializer
from .models import Notification, IssuedNotification


# Create your views here.
@api_view(['POST'])
def addnotification(request):
    data = JSONParser().parse(request)
    print(data)
    notification_serializer = IssuedNotificationSerializer(data=data)

    if notification_serializer.is_valid():
        print(notification_serializer.validated_data)
        notification_serializer.save()
    
    return Response({"status":"success"}, status=status.HTTP_200_OK)

@api_view(['GET'])
def getnotifications(request):
    data = JSONParser().parse(request)
    print(data)

    filter_notifications = IssuedNotification.objects.filter(user_id = int(data['userid']))
    get_notification_details = IssuedNotificationSerializer(filter_notifications, many=True)
    print(get_notification_details.data)

    notification_list = []

    for notification in filter_notifications:
        # if(notification.active):
        get_notification = Notification.objects.get(notification_id = notification.notification_id)
        serialized_notification = NotificationSerializer(get_notification)
        serialized_notification_details = IssuedNotificationSerializer(notification)

        dict_notification = {
            "notification": serialized_notification.data,
            "details": serialized_notification_details.data,
        }

        print(dict_notification)

        notification_list.append(dict_notification)

        

    return Response({"status": "success", "data": notification_list}, status=status.HTTP_200_OK)

