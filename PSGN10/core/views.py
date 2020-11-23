from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from core.models import AwayStats, HomeStats
from core.serializers import AwayStatsSerializer, HomeStatsSerializer
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
