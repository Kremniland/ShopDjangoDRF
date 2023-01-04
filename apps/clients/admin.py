from django.contrib import admin

from .models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['user', 'email_field', 'discount_type', 'address']
    ordering = ['user']

