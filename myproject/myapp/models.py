from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Goog(models.Model):
    objects = None
    title = models.CharField('Наименование', max_length=100)
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

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Comment(models.Model):
    objects = None
    title = models.CharField('Наименование', max_length=50)
    description = models.TextField('Описание')
    photo = models.ImageField(upload_to="photos", default=None, blank=True, null=True, verbose_name="Фото")

class Stat(models.Model):
    title = models.CharField(verbose_name='Название', max_length=60)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Orders(models.Model):
    created = models.DateTimeField(verbose_name='Дата',
                                   null=True)
    owner = models.ForeignKey('auth.User', verbose_name='Автор', related_name='orders_user',
                              on_delete=models.CASCADE,
                              null=True)
    prod = models.ForeignKey('Goog', verbose_name='Товары', related_name='orders_product', on_delete=models.CASCADE,
                             null=True)
    # position = models.ForeignKey('Position', verbose_name='Позиция', related_name='orders_position',
    #                              on_delete=models.CASCADE, null=True)
    description = models.TextField(verbose_name='Описание',
                                   null=True)
    stat = models.ForeignKey('Stat', verbose_name='Статус', related_name='orders_stat', on_delete=models.CASCADE,
                             null=True)
    price = models.ForeignKey('Goog', verbose_name='Товары', related_name='orders_price', on_delete=models.CASCADE,
                              null=True)
    service = models.ForeignKey('TypeOfService', verbose_name='Услуга', related_name='type_of_service', on_delete=models.CASCADE,
                              null=True)

    def __str__(self):
        return str(self.created)

    def get_absolute_url(self):
        return "/orders/%s" % self.owner.username
        # return "/orders/%i/" % self.id

    class Meta:
        ordering = ['created']
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

class TypeOfService(models.Model):
    title = models.CharField(verbose_name='Название', max_length=120)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Тип услуги'
        verbose_name_plural = 'Типы услуг'
