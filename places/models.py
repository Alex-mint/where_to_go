from django.db import models

class Place(models.Model):
    title = models.CharField('Название', max_length=255)
    description_short = models.TextField('Короткое описание')
    description_long = models.TextField('Полное описание')
    lng = models.DecimalField('Широта', max_digits=17, decimal_places=14)
    lat = models.DecimalField('Долгота', max_digits=17, decimal_places=14)

    def __str__(self):
        return self.title
