# usuarios/urls.py
from django.urls import path
from . import views
urlpatterns = [
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),
]