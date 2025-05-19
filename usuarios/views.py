from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import EditarPerfilForm, EditarPerfilFormAdicional
from django.contrib import messages
from .models import Perfil
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt


@login_required
def editar_perfil(request):
    try:
        perfil_usuario = request.user.perfil
    except ObjectDoesNotExist:
        perfil_usuario = Perfil(user=request.user)

    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, instance=request.user)
        perfil_form = EditarPerfilFormAdicional(request.POST, instance=perfil_usuario)
        if form.is_valid() and perfil_form.is_valid():
            form.save()
            perfil_form.save()
            messages.success(request, 'Tu perfil ha sido actualizado exitosamente.')
            return redirect('perfil_usuario')
        else:
            context = {
                'form': form,
                'perfil_form': perfil_form,
            }
            return render(request, 'usuarios/editar_perfil.html', context)
    else:
        form = EditarPerfilForm(instance=request.user)
        perfil_form = EditarPerfilFormAdicional(instance=perfil_usuario)
        context = {
            'form': form,
            'perfil_form': perfil_form,
        }
        return render(request, 'usuarios/editar_perfil.html', context)

@login_required
def perfil_usuario(request):
    usuario = request.user
    try:
        perfil = Perfil.objects.get(user=usuario)
    except Perfil.DoesNotExist:
        perfil = None  # Manejo si no existe el perfil

    context = {
        'usuario': usuario,
        'perfil': perfil,
    }
    return render(request, 'usuarios\perfil.html', context)  # Modifica la ruta de la plantilla
