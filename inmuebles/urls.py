from django.urls import path
from . import views

urlpatterns = [
    path('admin/propiedades/', views.listar_propiedades, name='listar_propiedades'),
    path('admin/propiedades/crear/', views.crear_propiedad, name='crear_propiedad'),
    path('admin/propiedades/editar/<int:pk>/', views.editar_propiedad, name='editar_propiedad'),
    path('admin/propiedades/eliminar/<int:pk>/', views.eliminar_propiedad, name='eliminar_propiedad'),
    path('inmuebles/', views.inmuebles_view, name='inmuebles'),  # Nueva ruta pública
]
