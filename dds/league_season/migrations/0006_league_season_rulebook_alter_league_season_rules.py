# Generated by Django 4.2.7 on 2024-01-22 22:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rules', '0001_initial'),
        ('league_season', '0005_league_season_champion'),
    ]

    operations = [
        migrations.AddField(
            model_name='league_season',
            name='ruleBook',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='league_season',
            name='rules',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rules.rules'),
        ),
    ]
