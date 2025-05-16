from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(label="Nombre", required=True)
    last_name = forms.CharField(label="Apellidos", required=True)
    email = forms.EmailField(label="Correo electrónico", required=True)

    class Meta:
        model = User
        fields = [
            "first_name", 
            "last_name", 
            "email", 
            "username", 
            "password1", 
            "password2"
        ]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        # afiliacion y pais no se guardan aquí porque no existen en el modelo User
        if commit:
            user.save()
        return user