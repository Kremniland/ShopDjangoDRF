from django.db import models
from versatileimagefield.fields import VersatileImageField


class Category(models.Model):
    '''Модель категорий'''
    title = models.CharField(max_length=64, verbose_name='Наименование')
    slug = models.SlugField(max_length=64)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    '''Товары'''
    title = models.CharField(max_length=128, verbose_name='Наименование')
    full_price = models.FloatField(verbose_name='Цена')
    description = models.CharField(max_length=512, verbose_name='Описание')
    amount = models.IntegerField(verbose_name='Колличество')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата поступления')
    exists = models.BooleanField(verbose_name='Есть ли в продаже')
    image = VersatileImageField(null=True, blank=True, upload_to='images/')
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='product'
        )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['title']


class Manufacturer(models.Model):
    '''Производитель'''
    title = models.CharField(max_length=100, verbose_name='Производитель')
    slug = models.SlugField(max_length=100)
    products = models.ManyToManyField(Product, blank=True, null=True, related_name='manufacturer')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'
