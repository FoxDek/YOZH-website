# Generated by Django 5.0.6 on 2024-05-29 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PartnerTicket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_name', models.CharField(max_length=255, verbose_name='Название организации')),
                ('director_name', models.CharField(max_length=255, verbose_name='Имя директора')),
                ('contact_phone', models.CharField(max_length=20, verbose_name='Телефон для связи')),
                ('work_email', models.EmailField(max_length=254, verbose_name='Рабочая почта')),
                ('comment', models.TextField(verbose_name='Комментарий')),
            ],
        ),
    ]