# ===================================================
# (De)Serializador de Horario
#
# Author: Tyron Fonseca - tyron.fonseca@ucr.ac.cr
# Last modified: 9/11/2021
# ===================================================

from rest_framework import serializers
from ferias.models import Horario
from api.serializers import feria_serializer as fs

class HorarioSerializer(serializers.ModelSerializer):
    ''' Serializador y deserializador del modelo Horario '''
    class Meta:
        model = Horario
        fields = ['feria', 'dia_inicio', 'hora_inicio', 'hora_final']
