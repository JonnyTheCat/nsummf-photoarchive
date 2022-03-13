from django.contrib import admin
from django.urls import path, include

from apps.base import urls as base_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(base_urls)),
]
