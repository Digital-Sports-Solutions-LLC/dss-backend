# Generated by Django 4.2.7 on 2023-12-22 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0003_alter_team_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='graphic',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
