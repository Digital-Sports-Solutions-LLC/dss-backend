# Generated by Django 4.2.7 on 2023-12-22 04:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0004_alter_team_graphic'),
        ('league_season', '0004_remove_league_season_champion'),
    ]

    operations = [
        migrations.AddField(
            model_name='league_season',
            name='champion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='team.team'),
        ),
    ]