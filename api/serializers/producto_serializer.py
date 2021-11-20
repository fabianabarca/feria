# ===================================================
# (De)Serializador de Producto
#
# Author: Tyron Fonseca - tyron.fonseca@ucr.ac.cr
# Last modified: 9/11/2021
# ===================================================

from rest_framework import serializers
from ferias.models import Producto


class ProductoSerializer(serializers.ModelSerializer):
    ''' Serializador y deserializador del modelo Producto '''
    class Meta:
        model = Producto
        fields = ['categoria', 'nombre_cientifico', 'nombre_comun', 'imagen', 
        'descripcion', 'temporada']
