from django.db import models
from django.utils.timezone import now


class AwayStats(models.Model):
    game_appearences = models.IntegerField(
        blank=True, verbose_name='Away game appearences')
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
    game_appearences = models.IntegerField(
        blank=True, verbose_name='Home game appearences')
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


class Player(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name='Player Name')
    first_name = models.CharField(max_length=100, blank=True,
                                  verbose_name='First Name')
    last_name = models.CharField(max_length=100, blank=True,
                                 verbose_name='Last Name')
    LEAGUE_CHOICES = (('Premier League', 'Premier League'),
                      ('Serie A', 'Serie A'),
                      ('LaLiga', 'LaLiga'),
                      ('BundesLiga', 'BundesLiga'),
                      ('Ligue 1', 'Ligue 1')
                      )
    league = models.CharField(choices=LEAGUE_CHOICES, max_length=100,
                              verbose_name='League')
    shirt_number = models.IntegerField(
        blank=True, verbose_name='Shirt Number')
    height = models.IntegerField(
        blank=True, verbose_name='Height in CM')
    positions = models.CharField(max_length=256, blank=True,
                                 verbose_name='Positions')
    current_team = models.CharField(max_length=100, blank=True,
                                    verbose_name='Current Team')
    date_of_birth = models.DateField(auto_now_add=False, blank=True)
    nationality = models.CharField(max_length=100, blank=True,
                                   verbose_name='Nationality')
    home_stats = models.OneToOneField(HomeStats, on_delete=models.CASCADE)
    away_stats = models.OneToOneField(AwayStats, on_delete=models.CASCADE)

