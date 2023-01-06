from django.urls import path, include
from rest_framework import routers


router = routers.DefaultRouter()
# router.register(r'api/clients', ClientViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]

