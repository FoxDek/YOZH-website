from django.db import models

class Event(models.Model):
    title = models.CharField('Название', max_length=255)
    description = models.TextField('Описание')
    coordinates_x = models.FloatField('Координата X')
    coordinates_y = models.FloatField('Координата Y')
    is_partner_event = models.BooleanField('Событие партнёров', default=False)

    def __str__(self):
        return self.title

class EventImage(models.Model):
    event = models.ForeignKey(Event, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='event_images/')

    def __str__(self):
        return self.image.url
