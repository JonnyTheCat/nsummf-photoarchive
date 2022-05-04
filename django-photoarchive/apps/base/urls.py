from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contacts/', views.contact, name="contacts"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
]
