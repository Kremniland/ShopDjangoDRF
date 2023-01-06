from django.db.models import Prefetch
from django.shortcuts import render

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from .models import Client
from .serializers import ClientSerializer


class ClientViewSet(ReadOnlyModelViewSet):
    ''' Вывод Client в апи с полями user__username user__email из модели User
    Забираем сразу user для снижения запросов serializer и поля только user__username user__email'''
    queryset = Client.objects.all().prefetch_related('user').only('user__username', 'user__email')
    # queryset = Client.objects.all().prefetch_related(
    #     Prefetch('user', queryset=Client.objects.all().prefetch_related('user')
    #              .only('user','user__email',)))
    serializer_class = ClientSerializer
    # Для авторизованных пользователей
    permission_classes = (IsAuthenticated, )
    # Только по токенам досуп
    authentication_classes = (TokenAuthentication, )

