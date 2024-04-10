from rest_framework import serializers
from accounts.models import Account

class LeaderboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['userid', 'username', 'rank', 'level', 'contribution']

class UserStatisticsSerializer(serializers.Serializer):
    user_id = serializers.CharField(max_length=100)
    # username = serializers.CharField(max_length=100)
    rank = serializers.IntegerField()
    contribution = serializers.IntegerField()
    level = serializers.IntegerField()
    completed_surveys_count = serializers.IntegerField()
    total_questions_answered = serializers.IntegerField()