"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
# proyecto_vehiculos_django/urls.py
from django.contrib import admin
from django.urls import path, include  # Importa include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('vehiculo/', include(('vehiculo.urls', 'vehiculo'), namespace = 'vehiculo')),  # Incluye las URLs de la aplicación vehiculo
    path('usuarios/', include(('usuarios.urls','usuarios'), namespace = 'usuarios')),
    path('', views.index, name='index'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
]