# Generated by Django 3.2.9 on 2021-12-03 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_rename_lan_places_lat'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Places',
            new_name='Place',
        ),
    ]
