# Generated by Django 4.2.7 on 2023-11-22 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0005_alter_match_livestreamlink'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='livestreamLink',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]