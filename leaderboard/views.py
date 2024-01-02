from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from accounts.models import Account
from leaderboard.serializers import LeaderboardSerializer

# Create your views here.
@api_view(['GET'])
def getranks(request):
 
    ranks = Account.objects.all()
    leaderboard_serializer  = LeaderboardSerializer(ranks, many=True)
    return Response({"status": "success", "data": leaderboard_serializer.data }, status=status.HTTP_200_OK)
  