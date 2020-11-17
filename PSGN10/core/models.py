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
