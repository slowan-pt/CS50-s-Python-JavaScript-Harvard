# Generated by Django 5.2.3 on 2025-06-11 00:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voos', '0002_airport_alter_flight_destination_alter_flight_orign'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flight',
            old_name='orign',
            new_name='origin',
        ),
    ]
