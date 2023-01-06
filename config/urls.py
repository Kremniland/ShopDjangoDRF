from django.contrib import admin
from django.urls import path, include, re_path

# Pillow (картинки)
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from apps.clients.views import ClientViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clients/', include('apps.clients.urls')),
    path('shop/', include('apps.shop.urls')),
    path('__debug__/', include('debug_toolbar.urls')),

    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

]

router = routers.DefaultRouter()
router.register(r'api/clients', ClientViewSet)

urlpatterns += router.urls

# Для статики:
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

