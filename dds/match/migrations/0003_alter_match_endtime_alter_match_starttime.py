# Generated by Django 4.2.7 on 2023-12-20 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0002_rename_court_match_court_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='endTime',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='match',
            name='startTime',
            field=models.TimeField(),
        ),
    ]
