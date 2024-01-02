from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import FAQ, Ticket
from helpsupport.serializers import FaqSerializer, TicketSerializer
 
# Create your views here.
@api_view(['GET'])
def getfaqs(request):
    faqs = FAQ.objects.all()
    serialized_faq = FaqSerializer(faqs, many=True)
    return Response({"status": "success", "faqs": serialized_faq.data}, status=status.HTTP_200_OK)
   
    
@api_view(['POST'])
def sendticket(request):
    ticket_data = JSONParser().parse(request)
    ticket_serializer = TicketSerializer(data = ticket_data)

    print(ticket_serializer)

    if ticket_serializer.is_valid():
        ticket_serializer.save()
        return Response({"status": "Ticket submitted"}, status=status.HTTP_201_CREATED)
    else:
        return Response(ticket_serializer.errors)

