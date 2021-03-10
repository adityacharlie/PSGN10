from .models import AwayStats, HomeStats, Player, League, LeagueTeam
from .serializers import AwayStatsSerializer, HomeStatsSerializer,\
    PlayerEditSerializer, LeagueSerializer, LeagueTeamSerializer
from accounts.permissions import IsCustomer


class AwayStatsAccessMixin(object):
    queryset = AwayStats.objects.all()
    serializer_class = AwayStatsSerializer


class HomeStatsAccessMixin(object):
    queryset = HomeStats.objects.all()
    serializer_class = HomeStatsSerializer


class LeagueAccessMixin(object):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer


class LeagueTeamAccessMixin(object):
    queryset = LeagueTeam.objects.all()
    serializer_class = LeagueTeamSerializer


class PlayerAccessMixin(object):
    queryset = Player.objects.all()
    serializer_class = PlayerEditSerializer
    permission_classes = IsCustomer,
