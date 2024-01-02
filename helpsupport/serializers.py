#The process of going from python object to JSON format
from rest_framework import serializers
from helpsupport.models import FAQ, Ticket

class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['faq_id', 'question', 'answer', 'category']


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['user_id', 'topic', 'body', 'category']