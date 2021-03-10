from core.models import AwayStats, HomeStats, Player, LeagueTeam, \
    League, Fixtures, Season, NationalTeam
from rest_framework import serializers


class AwayStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AwayStats
        fields = '__all__'


class HomeStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeStats
        fields = '__all__'


class LeagueTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeagueTeam
        fields = '__all__'


class PlayerAddSerializer(serializers.ModelSerializer):
    """
        Good example for Nested serializers
        Adding player with home and away stats at the same time

    """
    home_stats = HomeStatsSerializer(required=False, allow_null=True)
    away_stats = AwayStatsSerializer(required=False, allow_null=True)

    class Meta:
        model = Player
        fields = '__all__'

    def create(self, validated_data):

        home_stats_data = validated_data.pop('home_stats')
        away_stats_data = validated_data.pop('away_stats')
        league_ids = validated_data.pop('league_team')
        league_teams = LeagueTeam.objects.filter(pk__in=league_ids)

        if home_stats_data:
            player_home_stats = HomeStats.objects.create(
                **home_stats_data)
        else:
            player_home_stats = None

        if away_stats_data:
            player_away_stats = AwayStats.objects.create(
                **away_stats_data)
        else:
            player_away_stats = None

        player = Player.objects.create(
            home_stats=player_home_stats,
            away_stats=player_away_stats,
            **validated_data)

        player.league_team.set(league_teams)
        player.save()

        return player


class PlayerEditSerializer(serializers.ModelSerializer):
    home_stats = HomeStatsSerializer()
    away_stats = AwayStatsSerializer()

    class Meta:
        model = Player
        fields = '__all__'


class NationalTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = NationalTeam
        fields = '__all__'


class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = '__all__'


class AllLeagueSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)


class CreateFixturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fixtures
        fields = '__all__'


class FixturesListSerializer(serializers.ModelSerializer):
    key = serializers.SerializerMethodField()
    season = serializers.StringRelatedField()
    teamA = serializers.StringRelatedField()
    teamB = serializers.StringRelatedField()

    class Meta:
        model = Fixtures
        fields = '__all__'

    @staticmethod
    def get_key(instance):
        return instance.id


class CreateSeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = '__all__'


class AllSeasonSerializer(serializers.Serializer):
    name = serializers.SerializerMethodField()

    @staticmethod
    def get_name(instance):
        return instance.season
