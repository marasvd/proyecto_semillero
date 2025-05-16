"""
URL configuration for login project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from task import views
from django.urls import path, include
from django.contrib.auth import views as auth_views
from usuarios import views as usuarios_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    path('home/', views.home, name='home'),
    path('', views.home, name='home'),  # O quita esta si ya usas 'home/'
    path('revista/', include('revista.urls')),  # <- con prefijo
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('perfil/', views.perfil_usuario, name='perfil'),
    path('editar_perfil/', usuarios_views.editar_perfil, name='editar_perfil'),
    path('usuarios/', include('usuarios.urls')),
    path('task/', include('task.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


