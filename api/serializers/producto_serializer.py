# ===================================================
# (De)Serializador de Producto
#
# Author: Tyron Fonseca - tyron.fonseca@ucr.ac.cr
# Last modified: 9/11/2021
# ===================================================

from rest_framework.serializers import ModelSerializer
from drf_spectacular.utils import extend_schema_serializer
from ferias.models import Producto
from api.serializers.utils import DynamicFieldsSerializerMixin
from api.docs.examples.productos_examples import examples_productos_list


@extend_schema_serializer(
    examples=examples_productos_list
)
class ProductoSerializer(DynamicFieldsSerializerMixin, ModelSerializer):
    ''' Serializador y deserializador del modelo Producto '''
    class Meta:
        model = Producto
        fields = ['categoria', 'nombre_cientifico', 'nombre_comun', 'imagen',
                  'descripcion', 'temporada']
