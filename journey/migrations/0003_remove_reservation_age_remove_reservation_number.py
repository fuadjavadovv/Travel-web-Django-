# Generated by Django 4.1.3 on 2022-11-21 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journey', '0002_reservation_turn_reservation_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='age',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='number',
        ),
    ]
