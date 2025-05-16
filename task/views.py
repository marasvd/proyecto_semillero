from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db import IntegrityError
from .forms import CustomUserCreationForm
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .articulo_forms import EnviarArticuloForm
from django.contrib import messages

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': CustomUserCreationForm()
        })

    elif request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                # Verificar si el email ya existe
                if User.objects.filter(email=request.POST['email']).exists():
                    return render(request, 'signup.html', {
                        'form': CustomUserCreationForm(),
                        'error': 'Este correo electrónico ya está registrado'
                    })
                else:
                    # Crear el usuario
                    user = User.objects.create_user(
                        username=request.POST['username'],
                        email=request.POST['email'],
                        password=request.POST['password1'],
                        first_name=request.POST['first_name'],
                        last_name=request.POST['last_name'])

                    return redirect('home')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': CustomUserCreationForm(),
                    'error': 'Este usuario ya existe'
                })
        else:
            return render(request, 'signup.html', {
                'form': CustomUserCreationForm(),
                'error': 'Las contraseñas no coinciden'
            })


def home(request):
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def perfil_usuario(request):
    print(f"Usuario autenticado: {request.user.is_authenticated}")
    print(f"Tipo de request.user: {type(request.user)}")
    return render(request, 'perfil.html', {
        'usuario': request.user
})
@login_required
def enviar_articulo(request):
    if request.method == 'POST':
        form = EnviarArticuloForm(request.POST, request.FILES)
        if form.is_valid():
            articulo = form.save(commit=False)
            articulo.autor = request.user
            articulo.save()
            messages.success(request, 'Tu artículo ha sido enviado exitosamente.')
            return redirect('enviar_articulo') # Redirige a la misma página con mensaje
        else:
            messages.error(request, 'Hubo un error al enviar el artículo. Por favor, revisa el formulario.')
    else:
        form = EnviarArticuloForm()
    return render(request, 'task/enviar_articulo.html', {'form': form})