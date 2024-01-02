#The process of going from python object to JSON format
from rest_framework import serializers
from notifications.models import Notification, IssuedNotification

class IssuedNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssuedNotification
        fields = ['user_id', 'notification_id', 'priority', 'start_time', 'end_time',
                  'trigger_times']

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['notification_id', 'topic', 'text']
        