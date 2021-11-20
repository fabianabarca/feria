# ===================================================
# Clases encargadas del API relacionado a Producto
#
# Author: Tyron Fonseca - tyron.fonseca@ucr.ac.cr
# Last modified: 20/11/2021
# ===================================================

from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from ferias.models import Producto
from api.serializers.producto_serializer import ProductoSerializer
from api.views.utils import DynamicFieldsViewMixin


class ProductoList(DynamicFieldsViewMixin, generics.ListAPIView):
    ''' Metodos relacionados al modelo Producto, aqui se pueden
        crear productos.
    '''
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['temporada', 'categoria']
    search_fields = ['nombre_cientifico', 'nombre_comun', 'temporada',
                     'categoria', 'descripcion']


class ProductoDetail(DynamicFieldsViewMixin, generics.RetrieveAPIView):
    ''' Metodos relacionados al modelo Producto dado el ID del producto '''
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
