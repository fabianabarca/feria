# ===================================================
# Clases encargadas del API relacionado a Feria
#
# Last modified: 27/01/2022 - Tyron
# ===================================================

from django.http import Http404
from rest_framework.response import Response
from rest_framework import generics
from drf_spectacular.utils import extend_schema
from ferias.models import Horario
from api.serializers.horario_serializer import HorarioSerializer
from api.docs.params.horarios_params import horarios_params


class HorarioDetail(generics.RetrieveAPIView):
    ''' Metodos relacionados al modelo Horario dado el ID de la Feria '''

    def get_object(self, pk):
        '''Traer de la base de datos un horario dado el ID (pk) de la Feria'''
        try:
            return Horario.objects.filter(feria__feria_id=pk).all()
        except Horario.DoesNotExist:
            raise Http404

    def get_serializer_class(self):
        return HorarioSerializer

    @extend_schema(
        summary="horarios/{id}/",
        tags=['Horarios'],
        parameters=horarios_params)
    def get(self, request, pk):
        '''
        Get the Horarios (fair hours) of a specific Feria by their ID (pk)
        '''
        horario = self.get_object(pk)
        serializer = HorarioSerializer(horario, many=True)
        return Response(serializer.data)
