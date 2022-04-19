from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.api_photo_list, name='api_photo_list'),
    path('list/<int:photo_id>/', views.api_photo, name='api_photo'),
]
