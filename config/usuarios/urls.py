from django.urls import path
from . import views
from django.contrib import admin

app_name = 'usuarios'

urlpatterns = [
    path('registro/', views.registro ,name='registro'),
    
]