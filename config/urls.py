from django.contrib import admin
from django.urls import path, include

# Pillow (картинки)
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('clients/', include('apps.clients.urls')),
    path('shop/', include('apps.shop.urls')),
    path('__debug__/', include('debug_toolbar.urls')),

]

# Для статики:
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

