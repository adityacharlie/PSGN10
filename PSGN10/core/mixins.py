from .models import AwayStats, HomeStats
from .serializers import AwayStatsSerializer, HomeStatsSerializer


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
