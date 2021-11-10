# ===================================================
# (De)Serializador de Horario
#
# Author: Tyron Fonseca - tyron.fonseca@ucr.ac.cr
# Last modified: 9/11/2021
# ===================================================

from rest_framework import serializers
from ferias.models import Horario
from api.serializers import feria_serializer as fs

class HorarioSerializer(serializers.Serializer):
    ''' Serializador y deserializador del modelo Horario '''
    dia_inicio = serializers.CharField(max_length=1)
    hora_inicio = serializers.TimeField()
    dia_final = serializers.CharField(max_length=1)
    hora_final = serializers.TimeField()

    def create(self, validate_data):
        """
        Crear y retornar una instancia de Horario, con las validaciones
        """
        return Horario.objects.create(**validate_data)

    def update(self, instance, validate_data):
        """
        Actualizar y retornar una instancia de Horario, con las validaciones
        """
        instance.dia_inicio = validate_data.get(
            'dia_inicio', instance.dia_inicio)
        instance.hora_inicio = validate_data.get(
            'hora_inicio', instance.hora_inicio)
        instance.hora_final = validate_data.get(
            'hora_final', instance.hora_final)
        instance.dia_final = validate_data.get(
            'hora_final', instance.dia_final)        
        instance.save()
        return instance
