from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from apps.base import urls as base_urls
from apps.gallery import urls as gallery_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(base_urls)),
    path('', include(gallery_urls)),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)