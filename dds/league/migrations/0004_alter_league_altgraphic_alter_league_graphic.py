# Generated by Django 4.2.7 on 2023-12-21 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0003_rename_leagueid_league_league_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='league',
            name='altGraphic',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='league',
            name='graphic',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
