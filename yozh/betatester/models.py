from django.db import models

class BetaTesterTicket(models.Model):
    name = models.CharField('Имя', max_length=255)
    phone_number = models.CharField('Номер телефона', max_length=20)
    email = models.EmailField('Почта')

    def __str__(self):
        return self.name
