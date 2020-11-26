from core.models import AwayStats, HomeStats, Player
from rest_framework import serializers


class AwayStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AwayStats
        fields = '__all__'


class HomeStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeStats
        fields = '__all__'


class PlayerAddSerializer(serializers.ModelSerializer):
    '''
        Good example for Nested serializers
        Adding player with home and away stats at the same time

    '''
    home_stats = HomeStatsSerializer()
    away_stats = AwayStatsSerializer()

    class Meta:
        model = Player
        fields = '__all__'

    def create(self, validated_data):
        home_stats_data = validated_data.pop('home_stats')
        away_stats_data = validated_data.pop('away_stats')

        player_home_stats, phs = HomeStats.objects.get_or_create(
            **home_stats_data)
        player_away_stats, pas = AwayStats.objects.get_or_create(
            **away_stats_data)

        player = Player.objects.create(
            home_stats=player_home_stats,
            away_stats=player_away_stats,
            **validated_data)
        player.save()

        return player


class PlayerEditSerializer(serializers.ModelSerializer):
    home_stats = HomeStatsSerializer()
    away_stats = AwayStatsSerializer()

    class Meta:
        model = Player
        fields = '__all__'
