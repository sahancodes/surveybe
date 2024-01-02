from rest_framework import serializers
from accounts.models import Account

class LeaderboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['userid', 'rank', 'level', 'contribution']