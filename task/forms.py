from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

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
    def clean_password2(self):
        password = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password is not None and password != password2:
            raise ValidationError("Las contraseñas no coinciden")
        return password2

    def clean_password1(self):
        password = self.cleaned_data.get("password1")
        if len(password) < 8:
            raise ValidationError("La contraseña debe tener al menos 8 caracteres")
        if not any(char.isdigit() for char in password):
            raise ValidationError("La contraseña debe contener al menos un número")
        if not any(char.isalpha() for char in password):
            raise ValidationError("La contraseña debe contener al menos una letra")
        # Puedes agregar más validaciones aquí:
        # if not any(char.isupper() for char in password):
        #     raise ValidationError("La contraseña debe contener al menos una mayúscula")
        # if not any(char.islower() for char in password):
        #     raise ValidationError("La contraseña debe contener al menos una minúscula")
        # if not any(char in "!@#$%^&*()_+=-`~[]\{}|;':\",./<>?" for char in password):
        #     raise ValidationError("La contraseña debe contener al menos un símbolo")
        return password
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Este correo electrónico ya está registrado")
        return email
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("Este nombre de usuario ya existe")
        return username


    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        # afiliacion y pais no se guardan aquí porque no existen en el modelo User
        if commit:
            user.save()
        return user