# Generated by Django 4.2.7 on 2023-11-25 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0006_alter_match_livestreamlink'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='id',
        ),
        migrations.AddField(
            model_name='match',
            name='matchid',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
