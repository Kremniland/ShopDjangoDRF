from rest_framework import serializers

from clients.models import Client


class ClientSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user') # Создаем поле для имени, берем из User
    email_field = serializers.CharField(source='user.email') # Создаем поле для Email, берем из User

    class Meta:
        model = Client
        fields = ('id', 'user_name', 'email_field')
