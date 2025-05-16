from django.shortcuts import render
def home(request):
    return render(request, 'home.html')

def sobre_nosotros(request):
    return render(request, 'sobre_nosotros.html')

def archivos(request):
    return render(request, 'archivos.html')

def contacto(request):
    return render(request, 'contacto.html')

def equipo_editorial(request):
    return render(request, 'equipo_editorial.html')

def politicas(request):
    return render(request, 'politicas.html')

def instrucciones(request):
    return render(request, 'instrucciones.html')

def ediciones(request):
    return render(request, 'ediciones.html')

def enviar_articulo(request):
    return render(request, 'enviar_articulo.html')


# Create your views 
