# ===================================================
# Clases encargadas del API relacionado a Producto
#
# Author: Tyron Fonseca - tyron.fonseca@ucr.ac.cr
# Last modified: 29/11/2021
# ===================================================

from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from ferias.models import Producto
from api.serializers.producto_serializer import ProductoSerializer
from api.views.utils import DynamicFieldsViewMixin, optionalParams


@extend_schema(
    summary="productos/",
    tags=['Productos'],
    parameters=optionalParams)
class ProductoList(DynamicFieldsViewMixin, generics.ListAPIView):
    '''
    Return a list with all products
    '''
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['temporada', 'categoria']
    search_fields = ['nombre_cientifico', 'nombre_comun', 'temporada',
                     'categoria', 'descripcion']


@extend_schema(
    summary="productos/{id}/",
    tags=['Productos'],
    parameters=optionalParams)
class ProductoDetail(DynamicFieldsViewMixin, generics.RetrieveAPIView):
    '''
    Get a specific Producto by their ID (pk)
    '''
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
