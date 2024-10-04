#The process of going from python object to JSON format
from rest_framework import serializers
from accounts.models import Account, SurveyGroup
from django.contrib.auth.models import User


class AccountSerializer(serializers.ModelSerializer):
    class Meta:                                         #Meta data describing the model
        model = Account
        fields = ['userid','username', 'email', 'userimg', 
                  'age', 'gender', 'height', 'weight', 'best_hours',
                  'worksstarttime', 'workendtime', 'selfstatement',
                  'rank', 'level', 'contribution', 'created_on']

class UserSerializer(serializers.ModelSerializer):
    class Meta:                                         #Meta data describing the model
        model = User
        fields = ['username', 'email', 'password']

class InsertSerializer(serializers.ModelSerializer):
    class Meta:                                         #Meta data describing the model
        model = Account
        fields = ['username', 'email', 'age', 'gender', 'height', 'weight', 'best_hours',
                  'worksstarttime', 'workendtime', 'selfstatement']
        
class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['userid','username', 'email', 'userimg', 
                  'age', 'gender', 'height', 'weight', 'best_hours',
                  'worksstarttime', 'workendtime', 'selfstatement',
                  'rank', 'level', 'contribution', 'created_on']
        
class IsUserLoggedIn(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['authtoken']

class ForgotPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['email']

class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['email', 'age', 'gender', 'height', 'weight', 
                  'best_hours', 'worksstarttime', 'workendtime', 'selfstatement']

class SurveyGroupSerializer(serializers.ModelSerializer):
    # survey_id = serializers.IntegerField() 
    # start_date = serializers.DateField()
    # end_date = serializers.DateField()
    # trigger_times = serializers.JSONField()

    class Meta:
        model = SurveyGroup
        fields = ['survey_id', 'start_date', 'end_date', 'trigger_times']


class SurveyResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['rank', 'level', 'contribution']
