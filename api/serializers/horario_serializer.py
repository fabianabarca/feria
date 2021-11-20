# ===================================================
# (De)Serializador de Horario
#
# Author: Tyron Fonseca - tyron.fonseca@ucr.ac.cr
# Last modified: 20/11/2021
# ===================================================

from rest_framework.serializers import ModelSerializer
from ferias.models import Horario


class HorarioSerializer(ModelSerializer):
    ''' Serializador y deserializador del modelo Horario '''
    class Meta:
        model = Horario
        fields = ['dia_inicio', 'hora_inicio', 'dia_final', 'hora_final']
