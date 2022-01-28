# ===================================================
# (De)Serializador de Horario
#
# Author: Tyron Fonseca - tyron.fonseca@ucr.ac.cr
# Last modified: 02/12/2021
# ===================================================

from rest_framework.serializers import ModelSerializer
from drf_spectacular.utils import extend_schema_serializer
from ferias.models import Horario
from api.docs.examples.horarios_examples import examples_horarios_list


@extend_schema_serializer(
    examples=examples_horarios_list
)
class HorarioSerializer(ModelSerializer):
    ''' Serializador y deserializador del modelo Horario '''
    class Meta:
        model = Horario
        fields = ['dia_inicio', 'hora_inicio', 'dia_final', 'hora_final']
