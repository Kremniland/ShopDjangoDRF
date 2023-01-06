from rest_framework import serializers

from .models import Client, ContactModel


class ClientSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user') # Создаем поле для имени, берем из User
    email_field = serializers.CharField(source='user.email') # Создаем поле для Email, берем из User
    superuser = serializers.CharField(source='user.is_superuser')
    class Meta:
        model = Client
        fields = ('id', 'user_name', 'email_field', 'superuser')


class ContactModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactModel
        fields = ('__all__')
