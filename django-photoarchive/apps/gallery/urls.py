from django.urls import path
from . import views

urlpatterns = [
    path('gallery/', views.gallery, name="gallery"),
    path('gallery/id/<str:photo_id>/', views.photo, name="photo"),
]