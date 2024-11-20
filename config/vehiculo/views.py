from django.shortcuts import render, redirect, get_object_or_404
from .models import Vehiculo
from .forms import VehiculoForm
from django.contrib.auth.decorators import login_required, permission_required
from django.http import Http404



#@login_required()
#@permission_required('vehiculo.visualizar_vehiculo',raise_exception=True)
#def visualizar_vehiculo(request, vehiculo_id):
    #vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
    #if request.method == 'POST':
        #form=VehiculoForm(request.POST, instance=vehiculo)
        #if form.is_valid():
            #form.save()
            #return redirect('vehiculo:index')
    #else:
        #form=VehiculoForm(instance=vehiculo)
    #return render(request, 'vehiculo/listar.html',{'form':form}) 

@login_required()
@permission_required('vehiculo.agregar_vehiculo',raise_exception=True)
def agregar_vehiculo(request):
    # Código para manejar el formulario de agregar vehículo
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehiculo:index')  # Redirige a la página de inicio después de guardar
    else:
        form = VehiculoForm()

    return render(request, 'vehiculo/agregar_vehiculos.html', {'form': form})

@login_required()
#@permission_required('vehiculo.listar_vehiculos',raise_exception=True)
def listar_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    
    for vehiculo in vehiculos:
        if vehiculo.precio < 10000:
            vehiculo.rango_precio = "bajo"
        elif 10000 <= vehiculo.precio <= 30000:
            vehiculo.rango_precio = "medio"
        else:
            vehiculo.rango_precio = "alto"
    
    return render(request, 'vehiculo/listar.html', {'vehiculo': vehiculos})

def index(request):
    return render(request, 'vehiculo/index.html')



