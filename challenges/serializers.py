from rest_framework import serializers
from challenges.models import Challenge

class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = ['riddle_text', 'id']
