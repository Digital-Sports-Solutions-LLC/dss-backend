# Generated by Django 4.2.7 on 2023-12-20 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='match',
            old_name='court',
            new_name='court_event',
        ),
    ]
