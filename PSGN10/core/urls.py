from django.urls import path

from . import views

urlpatterns = [
    path('homestats/', views.HomeStatsLIst.as_view(), name='home_stats_list'),
    path('homestats/<int:pk>/', views.HomeStatsDetails.as_view(), name='home_stats_details'),
    path('awaystats/', views.AwayStatsLIst.as_view(), name='away_stats_list'),
    path('awaystats/<int:pk>/', views.AwayStatsDetails.as_view(), name='away_stats_details'),

    path('add/', views.AddPlayer.as_view(), name='add_player'),
    path('<int:pk>/', views.EditViewPlayer.as_view(), name='edit_view_player'),
    path('all/', views.AllPlayerList.as_view(), name='list_all_players'),

    path('league/add/', views.AddLeague.as_view(), name='add_league'),
    path('league/<int:pk>/', views.EditViewLeague.as_view(), name='edit_view_league'),
    path('leagueteam/add/', views.AddLeagueTeam.as_view(), name='add_league_team'),
    # path('leagueteam/all/', views.AllLeagueTeamList.as_view(), name='list_all_league_teams'),

]
