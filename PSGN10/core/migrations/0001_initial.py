# Generated by Django 3.1.3 on 2020-11-17 01:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AwayStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_appearences', models.IntegerField(blank=True, verbose_name='Away game appearences')),
                ('minutes_played', models.IntegerField(blank=True, verbose_name='Away minutes played')),
                ('goals_scored', models.IntegerField(blank=True, verbose_name='Away goals scored')),
                ('assists', models.IntegerField(blank=True, verbose_name='Away assists')),
                ('yellow_cards', models.IntegerField(blank=True, verbose_name='Away yellow cards')),
                ('red_cards', models.IntegerField(blank=True, verbose_name='Away red cards')),
                ('shots_per_game', models.DecimalField(blank=True, decimal_places=2, max_digits=5, verbose_name='Away shots per game')),
                ('man_of_the_match', models.IntegerField(blank=True, verbose_name='Away man of the match')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
            ],
        ),
    ]
