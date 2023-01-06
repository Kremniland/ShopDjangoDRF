from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Category, Product, Manufacturer
from .serializers import CategorySerializer


class CategotyViewSet(ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
