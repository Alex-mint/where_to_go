from django.db import models

class Place(models.Model):
    title = models.CharField('Название', max_length=255)
    placeId = models.CharField('ID места', max_length=255, null=True, blank=True)
    description_short = models.TextField('Короткое описание')
    description_long = models.TextField('Полное описание')
    lng = models.FloatField('Широта', default=0.0, blank=True)
    lat = models.FloatField('Долгота', default=0.0, blank=True)

    def __str__(self):
        return self.title

class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE,
        verbose_name="Место съёмки", null=True, blank=True)
    number = models.IntegerField('Номер картинки', null=True, blank=True)
    image = models.ImageField('Картинка', null=True, blank=True)

    def __str__(self):
        return f'{self.number}. {self.place.title}'
