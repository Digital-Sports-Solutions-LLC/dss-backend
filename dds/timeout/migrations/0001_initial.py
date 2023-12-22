# Generated by Django 4.2.7 on 2023-12-20 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('team', '0003_alter_team_active'),
        ('point', '0002_alter_point_endtime_alter_point_note_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TIMEOUT',
            fields=[
                ('timeout_ID', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=100)),
                ('note', models.CharField(max_length=200)),
                ('point', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='point.point')),
                ('takenBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='team.team')),
            ],
        ),
    ]