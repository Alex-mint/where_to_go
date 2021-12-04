from django.db import models

class Place(models.Model):
    title = models.CharField('Название', max_length=255)
    description_short = models.TextField('Короткое описание')
    description_long = models.TextField('Полное описание')
    lng = models.DecimalField('Широта', max_digits=17, decimal_places=14)
    lat = models.DecimalField('Долгота', max_digits=17, decimal_places=14)

    def __str__(self):
        return self.title

class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE,
        verbose_name="Место съёмки", null=True, blank=True)
    number = models.IntegerField('Номер картинки', null=True, blank=True)
    image = models.ImageField('Картинка', null=True, blank=True)

    def __str__(self):
        return f'{self.number}. {self.place.title}'
