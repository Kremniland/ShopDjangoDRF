from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Product, Manufacturer, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'full_price', 'amount', 'create_date', 'exists', 'category', 'image_show']
    ordering = ['title']

    def image_show(self, obj):
        '''Вывод маленькой картинки в админке'''
        if obj.image:
            return mark_safe("<img src='{}' width='60' />".format(obj.image.url))
        return None


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    ordering = ['title']


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['title']
    ordering = ['title']

