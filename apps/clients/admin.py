from django.contrib import admin
from .models import Client, ContactModel


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['user', 'discount_type', 'address']
    ordering = ['user']


@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'create_date']
    