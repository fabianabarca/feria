# ===================================================
# (De)Serializador de Feria
#
# Author: Tyron Fonseca - tyron.fonseca@ucr.ac.cr
# Last modified: 20/11/2021
# ===================================================

from rest_framework.serializers import ModelSerializer
from ferias.models import Feria
from api.serializers import producto_serializer as ps
from api.serializers import horario_serializer as hs
from api.serializers.utils import DynamicFieldsSerializerMixin


class FeriaSerializer(DynamicFieldsSerializerMixin, ModelSerializer):
    ''' Serializador y deserializador del modelo Feria '''

    # Declaramos explicitamente que serializador usar
    oferta = ps.ProductoSerializer(read_only=True, many=True)
    horarios = hs.HorarioSerializer(read_only=True, many=True)

    class Meta:
        model = Feria
        fields = '__all__'
