# ===================================================
# (De)Serializador de Feria
#
# Author: Tyron Fonseca - tyron.fonseca@ucr.ac.cr
# Last modified: 9/11/2021
# ===================================================

from rest_framework import serializers
from ferias.models import Producto, Feria
from api.serializers import producto_serializer as ps


class FeriaSerializer(serializers.ModelSerializer):
    ''' Serializador y deserializador del modelo Feria '''

    # Declaramos explicitamente que serializador tiene la oferta
    oferta = ps.ProductoSerializer(read_only=True, many=True)
    class Meta:
        model = Feria
        fields = ['ferias_id', 'codigo', 'nombre', 'provincia', 
        'canton', 'distrito', 'direccion', 'direccion', 
        'latitud', 'longitud', 'oferta']
