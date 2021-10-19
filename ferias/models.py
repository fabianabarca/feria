from django.db import models
from django.utils.translation import ugettext as _
from .utils import *

#===============================Productos====================================
class Producto(models.Model):
    nombre = models.CharField(max_length=60, primary_key=True)
    imagenRepresentativa = models.ImageField(
        upload_to='productos', blank=True, null=True)

    def __str__(self):
        return self.nombre

#===============================Telefono====================================
class Telefono(models.Model):
    telefono = models.CharField(
        validators=[telefonoRegex], max_length=15, primary_key=True)

    def __str__(self):
        return self.telefono

#===============================VENDEDORES=====================================
class Vendedor(models.Model):
    nombre = models.CharField(max_length=60)
    sitioWeb = models.URLField(max_length=100, blank=True, null=True)
    perfilInsta = models.URLField(max_length=100, blank=True, null=True)
    perfilFace = models.URLField(max_length=100, blank=True, null=True)
    logo = models.ImageField(
        upload_to='logos_vendedores', blank=True, null=True)
    productos = models.ManyToManyField(Producto)
    telefonos = models.ManyToManyField(Telefono)

    class Meta:
        verbose_name_plural = _('Vendedores')
    def __str__(self):
        return self.nombre

#===============================FERIAS=====================================
class Feria(models.Model):
    nombre = models.CharField(max_length=64)
    logo = models.ImageField(upload_to='logos_ferias', blank=True, null=True)
    distrito = models.CharField(max_length=60)
    canton = models.CharField(max_length=60)
    provincia = models.CharField(max_length=60)
    direccionExacta = models.CharField(max_length=260)
    lat = models.FloatField()
    lon = models.FloatField()
    horario = models.CharField(max_length=160)
    vendedores = models.ManyToManyField(Vendedor, blank=True, null=True)
    telefonos = models.ManyToManyField(Telefono, blank=True, null=True)
    productos = models.ManyToManyField(Producto, blank=True, null=True)
    def __str__(self):
        return self.nombre

