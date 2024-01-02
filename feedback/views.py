from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
from feedback.models import Feedback
from feedback.serializers import FeedbackSerializer

# Create your views here.
@api_view(['POST'])
def sendfeedback(request):
    feedback_data = JSONParser().parse(request)
    serialized_feedback = FeedbackSerializer(data=feedback_data)

    if serialized_feedback.is_valid():
        serialized_feedback.save()
        return Response({"status": "feedback saved"}, status=status.HTTP_200_OK)
    else:
        return Response({"status": "feedback error", "error": serialized_feedback.errors}, status=status.HTTP_400_BAD_REQUEST)
