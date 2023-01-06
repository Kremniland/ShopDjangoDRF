from django.urls import path, include
from rest_framework import routers

from .views import *


router = routers.DefaultRouter()
router.register(r'contacts', ContactViewSet)
router.register(r'clients', ClientViewSet)

urlpatterns = [
    path('123/', home_page),

    path('api/', include(router.urls)),
]

# urlpatterns += router.urls
