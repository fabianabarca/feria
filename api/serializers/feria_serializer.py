# ===================================================
# (De)Serializador de Feria
#
# Author: Tyron Fonseca - tyron.fonseca@ucr.ac.cr
# Last modified: 9/11/2021
# ===================================================

from rest_framework import serializers
from ferias.models import Producto
from api.serializers import producto_serializer as ps


class FeriaSerializer(serializers.Serializer):
    ''' Serializador y deserializador del modelo Feria '''
    ferias_id = serializers.CharField(max_length=3)
    codigo = serializers.CharField(max_length=30)
    nombre = serializers.CharField(max_length=128)
    provincia = serializers.IntegerField(max_value=6, min_value=0)
    canton = serializers.CharField(max_length=128)
    distrito = serializers.CharField(max_length=128)
    direccion = serializers.CharField()
    latitud = serializers.FloatField()
    longitud = serializers.FloatField()
    oferta = ps.ProductoSerializer(read_only=True, many=True)

    def create(self, validate_data):
        """
        Crear y retornar una instancia de Feria, con las validaciones
        """
        return Producto.objects.create(**validate_data)

    def update(self, instance, validate_data):
        """
        Actualizar y retornar una instancia de Feria, con las validaciones
        """
        instance.codigo = validate_data.get('codigo', instance.codigo)
        instance.nombre = validate_data.get('nombre', instance.nombre)
        instance.provincia = validate_data.get('provincia', instance.provincia)
        instance.canton = validate_data.get('canton', instance.canton)
        instance.distrito = validate_data.get('distrito', instance.distrito)
        instance.direccion = validate_data.get('direccion', instance.direccion)
        instance.latitud = validate_data.get('latitud', instance.latitud)
        instance.longitud = validate_data.get('longitud', instance.longitud)
        instance.save()
        return instance
