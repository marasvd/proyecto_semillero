from django.db import models
from django.contrib.auth.models import User

class Articulo(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    resumen = models.TextField()
    archivo = models.FileField(upload_to='articulos/')  # Guarda los archivos en la carpeta 'articulos/'
    fecha_envio = models.DateTimeField(auto_now_add=True)
    # Puedes agregar más campos como 'palabras_clave', 'area_tematica', etc.

    def __str__(self):
        return self.titulo
