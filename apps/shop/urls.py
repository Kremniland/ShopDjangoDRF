from django.urls import path, include
from rest_framework import routers

from .views import *


router = routers.DefaultRouter()
router.register(r'category', CategotyViewSet)

urlpatterns = [

    path('api/', include(router.urls)),
]

# urlpatterns += router.urls