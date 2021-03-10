from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView,\
    CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from core.models import AwayStats, HomeStats, Player, LeagueTeam, League, \
    Fixtures, Season, NationalTeam
from core.serializers import AwayStatsSerializer, HomeStatsSerializer,\
    PlayerAddSerializer, PlayerEditSerializer, LeagueTeamSerializer, \
    CreateFixturesSerializer, FixturesListSerializer, LeagueSerializer, \
    CreateSeasonSerializer, AllLeagueSerializer, AllSeasonSerializer, \
    NationalTeamSerializer
from core.mixins import AwayStatsAccessMixin, HomeStatsAccessMixin,\
    PlayerAccessMixin, LeagueAccessMixin, LeagueTeamAccessMixin


class HomeStatsLIst(ListAPIView):
    queryset = HomeStats.objects.all()
    serializer_class = HomeStatsSerializer
    pagination_class = None


class HomeStatsDetails(HomeStatsAccessMixin, RetrieveUpdateDestroyAPIView):
    """ get away stat details / update / delete """
    pass


class AwayStatsLIst(ListAPIView):
    queryset = AwayStats.objects.all()
    serializer_class = AwayStatsSerializer
    pagination_class = None


class AwayStatsDetails(AwayStatsAccessMixin, RetrieveUpdateDestroyAPIView):
    """ get away stat details / update / delete """
    pass


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
    pass


class AllPlayerList(ListAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerEditSerializer
    pagination_class = None


class AllLeagues(ListAPIView):
    queryset = League.objects.all()
    serializer_class = AllLeagueSerializer
    pagination_class = None


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
    pass


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
    pass


class AllLeagueTeamList(ListAPIView):
    queryset = LeagueTeam.objects.all()
    serializer_class = LeagueTeamSerializer
    pagination_class = None


class AddNationalTeam(CreateAPIView):
    queryset = NationalTeam.objects.all()
    serializer_class = NationalTeamSerializer
    pagination_class = None

    def create(self, request, * args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data,
                        status=status.HTTP_201_CREATED, headers=headers)


class AllNationalTeamList(ListAPIView):
    queryset = NationalTeam.objects.all()
    serializer_class = NationalTeamSerializer
    pagination_class = None


class AddFixture(CreateAPIView):
    queryset = Fixtures.objects.all()
    serializer_class = CreateFixturesSerializer
    pagination_class = None


class AllFixtures(ListAPIView):
    queryset = Fixtures.objects.all()
    serializer_class = FixturesListSerializer
    pagination_class = None


class AllSeasons(ListAPIView):
    queryset = Season.objects.all()
    serializer_class = AllSeasonSerializer
    pagination_class = None


class AddSeason(CreateAPIView):
    queryset = Season.objects.all()
    serializer_class = CreateSeasonSerializer
    pagination_class = None

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data,
                        status=status.HTTP_201_CREATED, headers=headers)
