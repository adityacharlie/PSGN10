from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView,\
    CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from core.models import AwayStats, HomeStats, Player
from core.serializers import AwayStatsSerializer, HomeStatsSerializer,\
    PlayerAddSerializer
from core.mixins import AwayStatsAccessMixin, HomeStatsAccessMixin


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
