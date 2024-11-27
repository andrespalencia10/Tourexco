# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Contactos(models.Model):
    id_contacto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    correo = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    mensaje = models.TextField(blank=True, null=True)
    fecha_contacto = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contactos'


class Imagenes(models.Model):
    id_imagen = models.AutoField(primary_key=True)
    url_imagen = models.CharField(max_length=255, blank=True, null=True)
    id_propiedad = models.ForeignKey('Propiedades', models.DO_NOTHING, db_column='id_propiedad', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'imagenes'


class Propiedades(models.Model):
    id_propiedad = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    codigo = models.CharField(max_length=10, blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ubicacion = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.CharField(max_length=20, blank=True, null=True)
    area_lote = models.FloatField(blank=True, null=True)
    area_construida = models.FloatField(blank=True, null=True)
    numero_habitaciones = models.SmallIntegerField(blank=True, null=True)
    numero_banos = models.SmallIntegerField(blank=True, null=True)
    numero_garaje = models.SmallIntegerField(blank=True, null=True)
    estado = models.BooleanField()
    imagen_principal = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'propiedades'


class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    correo = models.CharField(max_length=100, blank=True, null=True)
    contrasena = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuarios'
