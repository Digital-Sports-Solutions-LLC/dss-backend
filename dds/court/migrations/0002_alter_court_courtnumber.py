# Generated by Django 4.2.7 on 2023-12-20 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('court', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='court',
            name='courtNumber',
            field=models.PositiveIntegerField(),
        ),
    ]
