# Generated by Django 5.0 on 2024-01-27 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('point', '0002_alter_point_endtime_alter_point_note_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='point',
            name='gameClockEnd',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='point',
            name='gameClockStart',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
