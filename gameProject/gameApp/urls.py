from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('LogIn/', views.LogIn, name="LogIn"),
    path('about/', views.about, name="About"),
    path('contact/', views.contact, name="Contact"),
    path('play/', views.gamePlay, name="Play"),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)