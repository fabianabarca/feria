# ===================================================
# Clases encargadas del API relacionado a Feria
#
# Author: Tyron Fonseca - tyron.fonseca@ucr.ac.cr
# Last modified: 20/11/2021
# ===================================================

from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from ferias.models import Feria
from api.serializers.feria_serializer import FeriaSerializer
from api.views.utils import DynamicFieldsViewMixin


class FeriaList(DynamicFieldsViewMixin, generics.ListAPIView):
    ''' Retornar una lista con todas las ferias '''
    queryset = Feria.objects.all()
    serializer_class = FeriaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['provincia', 'canton', 'distrito',
                        'horarios__dia_inicio', 'horarios__dia_final',
                        'horarios__hora_inicio', 'horarios__hora_final']
    search_fields = ['nombre', 'provincia',
                     'canton', 'distrito', 'horarios__dia_inicio',
                     'horarios__dia_final']


class FeriaDetail(DynamicFieldsViewMixin, generics.RetrieveAPIView):
    '''Traer de la base de datos una feria dado su ID (pk)'''
    queryset = Feria.objects.all()
    serializer_class = FeriaSerializer
