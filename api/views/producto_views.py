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
from api.views.utils import DynamicFieldsViewMixin
from api.docs.params.parameters import optional_params
from api.docs.params.productos import productos_params


@extend_schema(
    summary="productos/",
    tags=['Productos'],
    parameters=optional_params+productos_params)
class ProductoList(DynamicFieldsViewMixin, generics.ListAPIView):
    '''
    Get a list with all the Productos. Some of the query parameters
    are used to filter the list. For example if we need to get
    the Productos given the `categoria` we put in the query the
    param: `?categoria=1`
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
    parameters=optional_params)
class ProductoDetail(DynamicFieldsViewMixin, generics.RetrieveAPIView):
    '''
    Get a specific Producto by their ID (pk)
    '''
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
