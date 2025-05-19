from django import forms
from django.contrib.auth.models import User
from .models import Perfil

class EditarPerfilForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, label='Nombre', required=False)
    last_name = forms.CharField(max_length=30, label='Apellido', required=False)
    email = forms.EmailField(label='Correo Electronico')
    username = forms.CharField(max_length=150, label='Nombre de Usuario')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['username']
        if commit:
            user.save()
        return user

class EditarPerfilFormAdicional(forms.ModelForm):
    telefono = forms.CharField(max_length=20, label='Teléfono', required=False)
    fecha_nacimiento = forms.DateField(label='Fecha de nacimiento', required=False, widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Perfil
        fields = ('telefono', 'fecha_nacimiento')