from django.db import models

# Create your models here.
class Comuna(models.Model):
    idComuna = models.IntegerField(primary_key=True, verbose_name="Id de comuna")
    nombreComuna = models.CharField(max_length=50, blank=True, verbose_name="Nombre de comuna")

    def __str__(self):
        return self.nombreComuna

class TipoSocio(models.Model):
    idSocio = models.IntegerField(primary_key=True, verbose_name="Id de socio")
    nombreSocio = models.CharField(max_length=50, blank=True, verbose_name="Nombre de socio")

    def __str__(self):
        return self.nombreSocio

class Asociado(models.Model):
    rutAsociado = models.CharField(primary_key=True, max_length=10, verbose_name="Rut del asociado")
    tipoAsociado = models.ForeignKey(TipoSocio, on_delete=models.CASCADE, verbose_name="Tipo de Asociado")
    nombre = models.CharField(max_length=100, blank=True, verbose_name="Nombre")
    correo = models.CharField(max_length=50, blank=True, verbose_name="Correo")
    edad = models.IntegerField(blank=True, verbose_name="Edad")
    telefono = models.IntegerField(blank=True, verbose_name="Teléfono")
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, verbose_name="Comuna")

    def __str__(self):
        return self.rutAsociado

class Producto(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="Codigo del producto")
    nombre = models.CharField(max_length=100, blank=True, verbose_name="Nombre de producto")
    precio = models.CharField(max_length=100, blank=True, verbose_name="Precio")
    foto=models.ImageField(upload_to="foto", null=True, blank=True, verbose_name="Foto")

    def __str__(self):
        return self.nombre
