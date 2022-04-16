from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name="gallery"),
    path('id/<str:photo_id>/', views.photo, name="photo"),
    path('list/', views.photo_list, name="list_of_photos"),
]