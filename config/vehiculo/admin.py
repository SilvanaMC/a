from django.contrib import admin
from .models import Vehiculo
from django.contrib.auth.models import Group, Permission

# Register your models here.
@admin.register(Vehiculo)

class OfertaAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'serial_carroceria', 'serial_motor', 'categoria', 'precio')
    search_fields = ('vehiculo__nombre', )
    
    def save_model(self,request, obj, form, change):
        group_admin = Group.objects.get(name='Administradores')
        permisos = Permission.objects.filter(codename__in=['agregar_vehiculo','listar_vehiculo'])
        
        group_admin.permissions.add(*permisos)