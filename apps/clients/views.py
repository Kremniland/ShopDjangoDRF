from django.db.models import Prefetch
from django.http import HttpResponse
from django.shortcuts import render

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from .models import Client, ContactModel
from .serializers import ClientSerializer, ContactModelSerializer
from .services import get_token


def home_page(request):
    '''Просто получаем токен из ф-ии в service и выводим его'''
    token = get_token('admin', '1234')
    return HttpResponse(token)


class ClientViewSet(ReadOnlyModelViewSet):
    ''' Вывод Client в апи с полями user__username user__email из модели User
    Забираем сразу user для снижения запросов serializer'''
    queryset = Client.objects.all().prefetch_related('user')
    # queryset = Client.objects.all().prefetch_related(
    #     Prefetch('user', queryset=Client.objects.all().prefetch_related('user')
    #              .only('user','user__email',)))
    serializer_class = ClientSerializer
    # Для авторизованных пользователей
    # permission_classes = (IsAuthenticated, )
    # Только по токенам досуп
    # authentication_classes = (TokenAuthentication, )


class ContactViewSet(ReadOnlyModelViewSet):
    queryset = ContactModel.objects.all()
    serializer_class = ContactModelSerializer

