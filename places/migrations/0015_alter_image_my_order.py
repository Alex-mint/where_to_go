# Generated by Django 3.2.9 on 2022-01-07 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0014_auto_20220107_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='my_order',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='Позиция'),
        ),
    ]
