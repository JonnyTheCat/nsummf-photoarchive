from django.contrib import admin
from django.urls import path, include

from apps.base import urls as base_urls
from apps.gallery import urls as gallery_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(base_urls)),
    path('gallery/', include(gallery_urls)),
]