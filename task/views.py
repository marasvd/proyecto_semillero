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
from django.contrib.auth import logout, login


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': CustomUserCreationForm()
        })

    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            try:
                user=form.save()
                login(request, user)  # Inicia sesión al usuario recién registrado
                return redirect('home')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': form,
                    'error': 'Este usuario ya existe'
                })
        else:
            return render(request, 'signup.html', {
                'form': form
            })

def home(request):
    user = request.user  # Obtiene el usuario autenticado
    context = {'user': user}  # Crea el contexto para el template
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