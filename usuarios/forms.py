# usuarios/forms.py
from django import forms
from django.contrib.auth.models import User

class EditarPerfilForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, label='Nombre', required=False)
    last_name = forms.CharField(max_length=30, label='Apellido', required=False)
    email = forms.EmailField(label='Correo Electrónico')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user