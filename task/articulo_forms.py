from django import forms
from .models import Articulo

class EnviarArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ('titulo', 'resumen', 'archivo')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['archivo'].widget = forms.FileInput() # Mejora la visualización del widget de archivo