#The process of going from python object to JSON format
from rest_framework import serializers
from feedback.models import Feedback

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['user_id', 'topic', 'body', 'category']