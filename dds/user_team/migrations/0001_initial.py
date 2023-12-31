# Generated by Django 4.2.7 on 2023-12-20 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('role', '0001_initial'),
        ('season', '0003_remove_season_league'),
        ('team', '0003_alter_team_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='USER_TEAM',
            fields=[
                ('user_team_ID', models.AutoField(primary_key=True, serialize=False)),
                ('number', models.PositiveBigIntegerField()),
                ('captain', models.BooleanField(default=True)),
                ('coach', models.BooleanField(default=True)),
                ('graphic', models.CharField(blank=True, max_length=100, null=True)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='role.role')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='season.season')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.team')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]
