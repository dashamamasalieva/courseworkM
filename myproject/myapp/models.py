from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Goog(models.Model):
    objects = None
    title = models.CharField('Наименование', max_length=50)
    description = models.TextField('Описание')
    price = models.FloatField('Цена', max_length=50)
    photo = models.ImageField(upload_to="photos", default=None, blank=True, null=True, verbose_name="Фото")

    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Reviews(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField('Содержание')

    def get_absolute_url(self):
        return reverse('reviews')


class Comment(models.Model):
    objects = None
    title = models.CharField('Наименование', max_length=50)
    description = models.TextField('Описание')
    photo = models.ImageField(upload_to="photos", default=None, blank=True, null=True, verbose_name="Фото")
