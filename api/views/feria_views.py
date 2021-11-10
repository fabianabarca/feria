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
from ferias.models import Feria
from api.serializers.feria_serializer import FeriaSerializer


class FeriaList(APIView):
    ''' Metodos relacionados al modelo Feria, aqui se pueden
        crear las ferias.
    '''

    def get(self, request):
        ''' Retornar una lista con todas las ferias '''
        productos = Feria.objects.all()
        serializer = FeriaSerializer(productos, many=True)
        return Response(serializer.data)

    # Esta funcionalidad no esta implementada todavia
    # def post(self, request, format=None):
    #     serializer = FeriaSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FeriaDetail(APIView):
    ''' Metodos relacionados al modelo Feria dado el ID de la Feria '''

    def get_object(self, pk):
        '''Traer de la base de datos una feria dado su ID (pk)'''
        try:
            return Feria.objects.get(ferias_id=pk)
        except Feria.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        '''Conseguir una feria dado su ID (pk)'''
        feria = self.get_object(pk)
        print(feria)
        serializer = FeriaSerializer(feria)
        return Response(serializer.data)

    # Estas funcionalidades no estan implementadas todavia
    # def put(self, request, pk, format=None):
    #     feria = self.get_object(pk)
    #     serializer = FeriaSerializer(feria, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk, format=None):
    #     feria = self.get_object(pk)
    #     feria.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
