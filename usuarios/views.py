# usuarios/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import EditarPerfilForm
from django.contrib import messages

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu perfil ha sido actualizado exitosamente.')
            return redirect('perfil_usuario')
    else:
        form = EditarPerfilForm(instance=request.user)
    return render(request, 'editar_perfil.html', {'form': form})  # <-- Cambia aquí

@login_required
def perfil_usuario(request):
    return render(request, 'perfil.html', {'usuario': request.user})  # <-- Asumiendo que tu archivo se llama perfil.html
