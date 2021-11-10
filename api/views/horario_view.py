# ===================================================
# Clases encargadas del API relacionado a Feria
#
# Author: Tyron Fonseca - tyron.fonseca@ucr.ac.cr
# Last modified: 9/11/2021
# ===================================================

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework import status
from ferias.models import Horario
from api.serializers.horario_serializer import HorarioSerializer


class HorarioDetail(APIView):
    ''' Metodos relacionados al modelo Horario dado el ID de la Feria '''

    def get_object(self, pk):
        '''Traer de la base de datos un horario dado el ID (pk) de la Feria'''
        try:
            return Horario.objects.filter(feria__ferias_id=pk).all()
        except Horario.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        '''Conseguir los horario de una Feria dado su ID (pk)'''
        horario = self.get_object(pk)
        print(horario)
        serializer = HorarioSerializer(horario, many=True)
        return Response(serializer.data)
