# Generated by Django 3.2.9 on 2021-12-04 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_rename_places_place'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(blank=True, null=True, verbose_name='Номер картинки')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Картинка')),
            ],
        ),
    ]