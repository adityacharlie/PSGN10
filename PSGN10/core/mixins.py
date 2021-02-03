from .models import AwayStats, HomeStats, Player, League, LeagueTeam
from .serializers import AwayStatsSerializer, HomeStatsSerializer,\
    PlayerEditSerializer, LeagueSerializer, LeagueTeamSerializer
from accounts.permissions import IsCustomer


class AwayStatsAccessMixin(object):
    queryset = AwayStats.objects.all()
    serializer_class = AwayStatsSerializer

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs


class HomeStatsAccessMixin(object):
    queryset = HomeStats.objects.all()
    serializer_class = HomeStatsSerializer

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs


class LeagueAccessMixin(object):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs

class LeagueTeamAccessMixin(object):
    queryset = LeagueTeam.objects.all()
    serializer_class = LeagueTeamSerializer

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs


class PlayerAccessMixin(object):
    queryset = Player.objects.all()
    serializer_class = PlayerEditSerializer
    permission_classes = IsCustomer,

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs
