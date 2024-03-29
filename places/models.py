from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Название', max_length=255)
    description_short = models.TextField('Короткое описание', blank=True)
    description_long = HTMLField('Полное описание', blank=True)
    lng = models.FloatField('Широта')
    lat = models.FloatField('Долгота')

    def __str__(self):
        return self.title

    class Meta(object):
        verbose_name = 'Место'
        verbose_name_plural = "Места"


class Image(models.Model):
    place = models.ForeignKey(
        Place, on_delete=models.CASCADE, related_name='images',
        verbose_name="Место съёмки"
    )
    image = models.ImageField('Картинка')
    order = models.PositiveIntegerField('Позиция', default=0, blank=True)

    def __str__(self):
        return f'{self.id}. {self.place.title}'

    class Meta(object):
        ordering = ['order']
        verbose_name = "Картинка"
        verbose_name_plural = "Картинки"
