#The process of going from python object to JSON format
from rest_framework import serializers
from surveys.models import Survey, Question, Answer, CompletedSurvey

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ['survey_id', 'survey_name', 'survey_intro', 'survey_intro',
                  'survey_type', 'unfolding_survey']
        
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['question_id', 'question_text', 'instruction', 'question_type', 'in_first_q_set']


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['answer_id', 'question_id','answers', 'unfoldings']


class CompletedSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompletedSurvey
        fields = ['survey_id', 'user_id', 'start_time', 'end_time', 'question_n_answer']
