from django.db import models
from django.utils.timezone import now


class AwayStats(models.Model):
    game_appearances = models.IntegerField(
        default=0, blank=True, verbose_name='Away game appearances')
    minutes_played = models.IntegerField(
        blank=True, verbose_name='Away minutes played')
    goals_scored = models.IntegerField(
        blank=True, verbose_name='Away goals scored')
    assists = models.IntegerField(
        blank=True, verbose_name='Away assists')
    yellow_cards = models.IntegerField(
        blank=True, verbose_name='Away yellow cards')
    red_cards = models.IntegerField(
        blank=True, verbose_name='Away red cards')
    shots_per_game = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True,
        verbose_name='Away shots per game')
    pass_success_percentage = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True,
        verbose_name='Away pass success percentage',
        default=0.0)
    aerials_won = models.DecimalField(
        blank=True, verbose_name='Away aerials won',
        max_digits=5, decimal_places=2, default=0.0)
    man_of_the_match = models.IntegerField(
        blank=True, verbose_name='Away man of the match')
    away_rating = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True,
        verbose_name='Away rating', default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=now, blank=True)


class HomeStats(models.Model):
    game_appearances = models.IntegerField(
        default=0, blank=True, verbose_name='Home game appearances')
    minutes_played = models.IntegerField(
        blank=True, verbose_name='Home minutes played')
    goals_scored = models.IntegerField(
        blank=True, verbose_name='Home goals scored')
    assists = models.IntegerField(
        blank=True, verbose_name='Home assists')
    yellow_cards = models.IntegerField(
        blank=True, verbose_name='Home yellow cards')
    red_cards = models.IntegerField(
        blank=True, verbose_name='Home red cards')
    shots_per_game = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True,
        verbose_name='Home shots per game')
    pass_success_percentage = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True,
        verbose_name='Home pass success percentage',
        default=0.0)
    aerials_won = models.DecimalField(
        blank=True, verbose_name='Home aerials won',
        max_digits=5, decimal_places=2, default=0.0)
    man_of_the_match = models.IntegerField(
        blank=True, verbose_name='Home man of the match')
    away_rating = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True,
        verbose_name='Home rating', default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=now, blank=True)


class League(models.Model):
    name = models.CharField(max_length=100, blank=True,
                            verbose_name='League Name')
    organising_body = models.CharField(max_length=100, blank=True,
                                       verbose_name='Organising Body')
    founded = models.DateField()
    country = models.CharField(max_length=100, blank=True,
                               verbose_name='Country')
    confederation = models.CharField(max_length=100, blank=True,
                                     verbose_name="Confederation")
    no_of_teams = models.IntegerField(blank=True, verbose_name='Number of Teams')


class Team(models.Model):
    name = models.CharField(max_length=100, blank=True,
                            verbose_name='Name')
    fullname = models.CharField(max_length=100, blank=True,
                                verbose_name='Full Name')
    nickname = models.CharField(max_length=100, blank=True,
                                verbose_name='Nick Name')
    shortname = models.CharField(max_length=100, blank=True,
                                 verbose_name='Short Name')
    head_coach = models.CharField(max_length=100, blank=True,
                                  verbose_name='Head Coach')
    ground = models.CharField(max_length=100, blank=True,
                              verbose_name='Ground')
    ground_capacity = models.IntegerField(
        blank=True, verbose_name='Ground Capacity')


class LeagueTeam(Team):
    founded = models.DateField(blank=True)
    president = models.CharField(max_length=100, blank=True,
                                 verbose_name='President')
    league = models.ForeignKey(League, on_delete=models.CASCADE)


class NationalTeam(Team):
    association = models.CharField(max_length=100, blank=True,
                                   verbose_name='Association')
    confederation = models.CharField(max_length=100, blank=True,
                                     verbose_name='confederation')
    fifa_code = models.CharField(max_length=100, blank=True,
                                 verbose_name='Fifa Code')
    captain = models.CharField(max_length=100, blank=True,
                               verbose_name='Captain')


class Player(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name='Player Name')
    first_name = models.CharField(max_length=100, blank=True,
                                  verbose_name='First Name')
    last_name = models.CharField(max_length=100, blank=True,
                                 verbose_name='Last Name')
    league_team = models.ManyToManyField(LeagueTeam, blank=True)
    national_team = models.OneToOneField(NationalTeam, on_delete=models.CASCADE)
    shirt_number = models.IntegerField(
        blank=True, verbose_name='Shirt Number')
    height = models.IntegerField(
        blank=True, verbose_name='Height in CM')
    positions = models.CharField(max_length=256, blank=True,
                                 verbose_name='Positions')
    date_of_birth = models.DateField(blank=True)
    nationality = models.CharField(max_length=100, blank=True,
                                   verbose_name='Nationality')
    home_stats = models.OneToOneField(HomeStats, on_delete=models.CASCADE)
    away_stats = models.OneToOneField(AwayStats, on_delete=models.CASCADE)
