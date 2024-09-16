from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, authentication_classes, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.shortcuts import get_object_or_404
from surveys.models import Survey, Question, Answer, CompletedSurvey
from accounts.models import Account
from datetime import date
from surveys.serializer import SurveySerializer, QuestionSerializer, AnswerSerializer, CompletedSerializer
from accounts.serializers import SurveyResponseSerializer
import logging

# Set up logging
logger = logging.getLogger(__name__)

# Create your views here.
@api_view(['POST'])
def getsurvey(request):
    survey_req = JSONParser().parse(request)
    
    try:
        survey = get_object_or_404(Survey, survey_id=int(survey_req['survey_id']))
        questions = Question.objects.filter(survey_index = survey.survey_id)

        answers = Answer.objects.filter(question_id__in =questions.values_list('question_id', flat=True))
        print(answers)
        
        survey_serializer = SurveySerializer(survey)
        question_serializer = QuestionSerializer(questions, many=True)
        answer_serializer = AnswerSerializer(answers, many = True)

        return Response({"status": "success", "survey": survey_serializer.data, 
                        "questions": question_serializer.data, "answers": answer_serializer.data}, 
                        status=status.HTTP_200_OK)

    except Survey.DoesNotExist:
        return Response({"status": "Survey not found"}, status=status.HTTP_404_NOT_FOUND)
    except ValueError as e:
        logger.error(f"ValueError: {e}")
        return Response({"status": "Invalid survey_id"}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return Response({"status": "bad request"}, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def savesurvey(request):

    # try:
    data = JSONParser().parse(request)
    print(data)
    completed_survey_serializer = CompletedSerializer(data=data)
    additional_data = {
        'date': date.today(),
    }

    if completed_survey_serializer.is_valid():
        completed_survey_serializer.save(**additional_data)
        user_object = Account.objects.get(pk=int(completed_survey_serializer.data['user_id']))
        survey_object = Survey.objects.get(survey_id = completed_survey_serializer.data['survey_id'])
        user_object.update_contribution(user_object.userid, survey_object.survey_id)
        user_object.update_levels(user_object.userid)
        user_object.update_ranks()
        
        return Response({"status":"success", "userid": user_object.userid, "level": user_object.level, 
                         "rank": user_object.rank, "contribution": user_object.contribution}, 
                         status=status.HTTP_200_OK)
    else:
        return Response({"status": "invalid serializer", "error": completed_survey_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    # except:
    #     return Response({"status": "survey error"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['Get'])
def getsurveydetails(request):

    allsurveys = Survey.objects.all()
    serializer = SurveySerializer(allsurveys, many=True)

    return Response({'all_surveys':serializer.data}, status=200)


@api_view(['Get'])
def checksubmission(request, surveyid, userid):
    surveysubmitted = CompletedSurvey.is_survey_submitted(surveyid, userid)

    return Response({"submitted": surveysubmitted}, status=200)
