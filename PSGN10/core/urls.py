from django.urls import path

from . import views

urlpatterns = [
    path('player/homestats/', views.HomeStatsLIst.as_view(), name='home_stats_list'),
    path('player/homestats/<int:pk>/', views.HomeStatsDetails.as_view(), name='home_stats_details'),
    path('player/awaystats/', views.AwayStatsLIst.as_view(), name='away_stats_list'),
    path('player/awaystats/<int:pk>/', views.AwayStatsDetails.as_view(), name='away_stats_details'),

    path('player/add/', views.AddPlayer.as_view(), name='add_player'),
    path('player/<int:pk>/', views.EditViewPlayer.as_view(), name='edit_view_player'),
    path('player/all/', views.AllPlayerList.as_view(), name='list_all_players'),

    path('league/add/', views.AddLeague.as_view(), name='add_league'),
    path('league/all/', views.AllLeagues.as_view(), name='all_leagues'),
    path('league/<int:pk>/', views.EditViewLeague.as_view(), name='edit_view_league'),

    path('leagueteam/add/', views.AddLeagueTeam.as_view(), name='add_league_team'),
    path('leagueteam/<int:pk>/', views.EditViewLeagueTeam.as_view(), name='edit_view_league_team'),
    path('leagueteam/all/', views.AllLeagueTeamList.as_view(), name='list_all_league_teams'),

    path('nationalteam/add/', views.AddNationalTeam.as_view(), name='add_national_team'),
    # path('nationalteam/<int:pk>/', views.EditViewNationalTeam.as_view(), name='edit_view_national_team'),
    path('nationalteam/all/', views.AllNationalTeamList.as_view(), name='list_all_national_teams'),

    path('fixtures/add/', views.AddFixture.as_view(), name='add_fixture'),
    path('fixtures/all/', views.AllFixtures.as_view(), name='all_fixtures'),

    path('season/add/', views.AddSeason.as_view(), name='add_season'),
    path('season/all/', views.AllSeasons.as_view(), name='all_seasons'),

]
