# ===================================================
# Clases encargadas del API relacionado a Producto
#
# Author: Tyron Fonseca - tyron.fonseca@ucr.ac.cr
# Last modified: 9/11/2021
# ===================================================

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework import status
from ferias.models import Producto
from api.serializers.producto_serializer import ProductoSerializer


class ProductoList(APIView):
    ''' Metodos relacionados al modelo Producto, aqui se pueden
        crear productos.
    '''
    def get(self, request):
        ''' Retornar una lista con todos los productos '''
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)

    # Esta funcionalidad no esta implementada todavia
    # def post(self, request, format=None):
    #     serializer = ProductoSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductoDetail(APIView):
    ''' Metodos relacionados al modelo Producto dado el ID del producto '''
    def get_object(self, pk):
        '''Traer de la base de datos un producto dado su ID (pk)'''
        try:
            return Producto.objects.get(pk=pk)
        except Producto.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        '''Conseguir un producto dado su ID (pk)'''
        producto = self.get_object(pk)
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)

    # Estas funcionalidades no estan implementadas todavia
    # def put(self, request, pk, format=None):
    #     producto = self.get_object(pk)
    #     serializer = ProductoSerializer(producto, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # def delete(self, request, pk, format=None):
    #     producto = self.get_object(pk)
    #     producto.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
