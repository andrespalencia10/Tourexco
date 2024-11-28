# inmuebles/forms.py
from django import forms
from .models import Propiedades

class PropiedadForm(forms.ModelForm):
    class Meta:
        model = Propiedades
        fields = [
            'titulo', 'descripcion', 'codigo', 'precio', 'ubicacion', 'tipo',
            'area_lote', 'area_construida', 'numero_habitaciones', 'numero_banos',
            'numero_garaje', 'estado', 'imagen_principal'
        ]
