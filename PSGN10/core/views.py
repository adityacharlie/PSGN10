from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView,\
    CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from core.models import AwayStats, HomeStats, Player, LeagueTeam, League
from core.serializers import AwayStatsSerializer, HomeStatsSerializer,\
    PlayerAddSerializer, PlayerEditSerializer, LeagueTeamSerializer, LeagueSerializer
from core.mixins import AwayStatsAccessMixin, HomeStatsAccessMixin,\
    PlayerAccessMixin, LeagueAccessMixin, LeagueTeamAccessMixin


class HomeStatsLIst(ListAPIView):
    queryset = HomeStats.objects.all()
    serializer_class = HomeStatsSerializer
    pagination_class = None

    def get_queryset(self):
        return super().get_queryset()


class HomeStatsDetails(HomeStatsAccessMixin, RetrieveUpdateDestroyAPIView):
    """ get away stat details / update / delete """

    def get_queryset(self):
        return super().get_queryset()


class AwayStatsLIst(ListAPIView):
    queryset = AwayStats.objects.all()
    serializer_class = AwayStatsSerializer
    pagination_class = None

    def get_queryset(self):
        return super().get_queryset()


class AwayStatsDetails(AwayStatsAccessMixin, RetrieveUpdateDestroyAPIView):
    """ get away stat details / update / delete """

    def get_queryset(self):
        return super().get_queryset()


class AddPlayer(CreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerAddSerializer
    pagination_class = None

    def create(self, request, * args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data,
                        status=status.HTTP_201_CREATED, headers=headers)


class EditViewPlayer(PlayerAccessMixin, RetrieveUpdateDestroyAPIView):

    def get_queryset(self):
        return super().get_queryset()


class AllPlayerList(ListAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerEditSerializer
    pagination_class = None

    def get_queryset(self):
        return super().get_queryset()


class AddLeague(CreateAPIView):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer
    pagination_class = None

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data,
                        status=status.HTTP_201_CREATED, headers=headers)


class EditViewLeague(LeagueAccessMixin, RetrieveUpdateDestroyAPIView):

    def get_queryset(self):
        return super().get_queryset()


class AddLeagueTeam(CreateAPIView):
    queryset = LeagueTeam.objects.all()
    serializer_class = LeagueTeamSerializer
    pagination_class = None

    def create(self, request, * args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data,
                        status=status.HTTP_201_CREATED, headers=headers)


class EditViewLeagueTeam(LeagueTeamAccessMixin, RetrieveUpdateDestroyAPIView):

    def get_queryset(self):
        return super().get_queryset()


class AllLeagueTeamList(ListAPIView):
    queryset = LeagueTeam.objects.all()
    serializer_class = LeagueTeamSerializer
    pagination_class = None

    def get_queryset(self):
        return super().get_queryset()
