# Generated by Django 3.2.9 on 2021-12-05 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_place_placeid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='lat',
            field=models.DecimalField(decimal_places=17, max_digits=20, verbose_name='Долгота'),
        ),
        migrations.AlterField(
            model_name='place',
            name='lng',
            field=models.DecimalField(decimal_places=17, max_digits=20, verbose_name='Широта'),
        ),
    ]
