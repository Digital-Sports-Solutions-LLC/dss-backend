# Generated by Django 4.2.7 on 2023-12-20 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('season', '0002_rename_leagueid_season_league_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='season',
            name='league',
        ),
    ]
