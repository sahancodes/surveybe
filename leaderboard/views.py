from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from accounts.models import Account
from leaderboard.serializers import LeaderboardSerializer, UserStatisticsSerializer
from surveys.models import CompletedSurvey

# Create your views here.
@api_view(['GET'])
def getranks(request):
 
    ranks = Account.objects.all()
    leaderboard_serializer  = LeaderboardSerializer(ranks, many=True)
    return Response({"status": "success", "data": leaderboard_serializer.data }, status=status.HTTP_200_OK)

@api_view(['GET'])
def getleaders(request):

    leaderstats = []
    leaders = Account.objects.all()

    for leader in leaders:
        try:
            # Calculate completed_surveys_count and total_questions_answered for each user
            completed_surveys = CompletedSurvey.objects.filter(user_id=leader)
            completed_surveys_count = completed_surveys.count()
            total_questions_answered = sum(len(survey.question_n_answer) for survey in completed_surveys)

            leader_data = {
                'user_id': leader.userid.username,
                # 'username': leader.userid.username,
                # Assume 'rank' and 'contribution' are attributes or can be calculated
                'rank': getattr(leader, 'rank', 0),  # Default to 0 if not exists
                'contribution': getattr(leader, 'contribution', 0),  # Default to 0 if not exists
                'level': leader.level,
                'completed_surveys_count': completed_surveys_count,
                'total_questions_answered': total_questions_answered,
            }

            leaderstats.append(leader_data)

        except Exception as e:
            # Handle any other exception that might occur
            print(f"An error occurred for user {leader.userid}: {e}")
            continue

    #Serialize the data
    serializer = UserStatisticsSerializer(leaderstats, many=True)
    return Response({"status": "success", "data": serializer.data }, status=status.HTTP_200_OK)

