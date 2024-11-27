# inmuebles/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Propiedades
from .forms import PropiedadForm

def listar_propiedades(request):
    propiedades = Propiedades.objects.all()
    return render(request, 'admin/listar_propiedades.html', {'propiedades': propiedades})

def crear_propiedad(request):
    if request.method == 'POST':
        form = PropiedadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_propiedades')
    else:
        form = PropiedadForm()
    return render(request, 'admin/crear_propiedad.html', {'form': form})

def editar_propiedad(request, pk):
    propiedad = get_object_or_404(Propiedades, pk=pk)
    if request.method == 'POST':
        form = PropiedadForm(request.POST, instance=propiedad)
        if form.is_valid():
            form.save()
            return redirect('listar_propiedades')
    else:
        form = PropiedadForm(instance=propiedad)
    return render(request, 'admin/editar_propiedad.html', {'form': form})

def eliminar_propiedad(request, pk):
    propiedad = get_object_or_404(Propiedades, pk=pk)
    if request.method == 'POST':
        propiedad.delete()
        return redirect('listar_propiedades')
    return render(request, 'admin/eliminar_propiedad.html', {'propiedad': propiedad})

def inmuebles_view(request):
    propiedades = Propiedades.objects.all()  # Obtener todas las propiedades
    return render(request, 'inmuebles/listado.html', {'propiedades': propiedades})

