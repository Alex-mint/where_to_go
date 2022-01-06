from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Название', max_length=255)
    placeId = models.CharField('ID места', max_length=255, null=True, blank=True)
    description_short = models.TextField('Короткое описание')
    description_long = HTMLField('Полное описание')
    lng = models.FloatField('Широта', default=0.0, blank=True)
    lat = models.FloatField('Долгота', default=0.0, blank=True)

    def __str__(self):
        return self.title

    class Meta(object):
        verbose_name = 'Место'
        verbose_name_plural = "Места"


class Image(models.Model):
    place = models.ForeignKey(
        Place, on_delete=models.CASCADE, related_name='images',
        verbose_name="Место съёмки", null=True, blank=True
    )
    number = models.IntegerField('Позиция', null=True, blank=True)
    image = models.ImageField('Картинка', null=True, blank=True)
    my_order = models.PositiveIntegerField('Позиция', default=0)

    def __str__(self):
        return f'{self.number}. {self.place.title}'


    class Meta(object):
        ordering = ['my_order']
        verbose_name = "Картинка"
        verbose_name_plural = "Картинки"

