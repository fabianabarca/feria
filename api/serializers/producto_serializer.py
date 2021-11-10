# ===================================================
# (De)Serializador de Producto
#
# Author: Tyron Fonseca - tyron.fonseca@ucr.ac.cr
# Last modified: 9/11/2021
# ===================================================

from rest_framework import serializers
from ferias.models import Producto


class ProductoSerializer(serializers.Serializer):
    ''' Serializador y deserializador del modelo Producto '''
    id = serializers.IntegerField(read_only=True)
    nombre_cientifico = serializers.CharField(max_length=128, allow_blank=True)
    nombre_comun = serializers.CharField(max_length=128)
    descripcion = serializers.CharField()
    temporada = serializers.CharField()
    categoria = serializers.IntegerField(max_value=5, min_value=0)
    imagen = serializers.ImageField(allow_empty_file=True)
    icono = serializers.ImageField(allow_empty_file=True)

    def create(self, validate_data):
        """
        Crear y retornar una instancia de Producto, con las validaciones
        """
        return Producto.objects.create(**validate_data)

    def update(self, instance, validate_data):
        """
        Actualizar y retornar una instancia de Producto, con las validaciones
        """
        instance.categoria = validate_data.get('categoria', instance.categoria)
        instance.nombre_cientifico = validate_data.get(
            'nombre_cientifico', instance.nombre_cientifico)
        instance.nombre_comun = validate_data.get(
            'nombre_comun', instance.nombre_comun)
        instance.descripcion = validate_data.get(
            'descripcion', instance.descripcion)
        instance.temporada = validate_data.get('temporada', instance.temporada)
        instance.imagen = validate_data.get('imagen', instance.imagen)
        instance.icono = validate_data.get('icono', instance.icono)
        instance.save()
        return instance
