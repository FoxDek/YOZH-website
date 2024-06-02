# Generated by Django 5.0.6 on 2024-06-01 19:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Walk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('places', models.IntegerField(verbose_name='Количество мест')),
                ('hours_duration', models.FloatField(verbose_name='Длительность')),
            ],
        ),
        migrations.CreateModel(
            name='WalkImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='walk_images/')),
                ('walk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='walks.walk')),
            ],
        ),
    ]