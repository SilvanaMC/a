from django.urls import path
from . import views

app_name = 'vehiculo'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.agregar_vehiculo, name='agregar_vehiculos'),
    path('list/', views.listar_vehiculos, name='listar'), 
]
