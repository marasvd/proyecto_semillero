# task/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('enviar_articulo/', views.enviar_articulo, name='enviar_articulo'),
    # Otras URLs específicas de la aplicación 'task'
]
