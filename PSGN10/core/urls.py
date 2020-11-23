from django.urls import path

from . import views

urlpatterns = [
    path('homestats/', views.HomeStatsLIst.as_view(), name='home_stats_list'),
    path('homestats/<int:pk>/', views.HomeStatsDetails.as_view(), name='home_stats_details'),
    path('awaystats/', views.AwayStatsLIst.as_view(), name='away_stats_list'),
    path('awaystats/<int:pk>/', views.AwayStatsDetails.as_view(), name='away_stats_details'),

    path('player/add/', views.AddPlayer.as_view(), name='add_player'),
]
