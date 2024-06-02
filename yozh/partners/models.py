from django.db import models

class PartnerTicket(models.Model):
    organization_name = models.CharField('Название организации', max_length=255)
    director_name = models.CharField('Имя директора', max_length=255)
    contact_phone = models.CharField('Телефон для связи', max_length=20)
    work_email = models.EmailField('Рабочая почта')
    comment = models.TextField('Комментарий')

    def __str__(self):
        return self.organization_name

