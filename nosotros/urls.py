from django.urls import path
from . import views

urlpatterns = [
    path('', views.quienes_somos, name='nosotros'),
]
