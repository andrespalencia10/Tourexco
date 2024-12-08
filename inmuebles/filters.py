import django_filters
from .models import Propiedades

class PropiedadesFilter(django_filters.FilterSet):
    precio_min = django_filters.NumberFilter(field_name="precio", lookup_expr="gte")
    precio_max = django_filters.NumberFilter(field_name="precio", lookup_expr="lte")
    area_lote_min = django_filters.NumberFilter(field_name="area_lote", lookup_expr="gte")
    area_lote_max = django_filters.NumberFilter(field_name="area_lote", lookup_expr="lte")
    habitaciones = django_filters.NumberFilter(field_name="numero_habitaciones")
    banos = django_filters.NumberFilter(field_name="numero_banos")
    garaje = django_filters.BooleanFilter(field_name="numero_garaje", lookup_expr="gte")
    tipo = django_filters.ChoiceFilter(field_name="tipo", choices=Propiedades.TIPO_CHOICES)  # Cambia según tu modelo

    class Meta:
        model = Propiedades
        fields = [
            "titulo",
            "descripcion",
            "codigo",
            "ubicacion",
            "estado",
        ]



