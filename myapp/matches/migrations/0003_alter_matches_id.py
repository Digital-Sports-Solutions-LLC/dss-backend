# Generated by Django 4.2.7 on 2023-11-22 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0002_alter_matches_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matches',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]