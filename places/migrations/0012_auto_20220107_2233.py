# Generated by Django 3.2.9 on 2022-01-07 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0011_auto_20220107_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='lat',
            field=models.FloatField(verbose_name='Долгота'),
        ),
        migrations.AlterField(
            model_name='place',
            name='lng',
            field=models.FloatField(verbose_name='Широта'),
        ),
    ]
