from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),  # Cambiado de 'inicio' a 'home'
    path('sobre-nosotros/', views.sobre_nosotros, name='sobre_nosotros'),
    path('archivos/', views.archivos, name='archivos'),
    path('contacto/', views.contacto, name='contacto'),
    path('equipo-editorial/', views.equipo_editorial, name='equipo_editorial'),
    path('politicas/', views.politicas, name='politicas'),
    path('enviar-articulo/', views.enviar_articulo, name='enviar_ariculo'),

]

