from django.db import models


class Walk(models.Model):
    title = models.CharField('Название', max_length=255)
    description = models.TextField('Описание')
    places = models.IntegerField('Количество мест')
    hours_duration = models.FloatField('Длительность')

    def __str__(self):
        return self.title


class WalkImage(models.Model):
    walk = models.ForeignKey(Walk, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='walk_images/')

    def __str__(self):
        return self.image.name
