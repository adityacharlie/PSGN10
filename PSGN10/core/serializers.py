from core.models import AwayStats, HomeStats
from rest_framework import serializers


class AwayStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AwayStats
        fields = '__all__'


class HomeStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeStats
        fields = '__all__'
