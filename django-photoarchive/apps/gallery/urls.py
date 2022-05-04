from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name="gallery"),
    path('id/<int:photo_id>/', views.photo, name="photo"),
    path('upload-photo/', views.upload_photo, name="add_photo"),
]