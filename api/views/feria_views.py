# ===================================================
# Clases encargadas del API relacionado a Feria
#
# Author: Tyron Fonseca - tyron.fonseca@ucr.ac.cr
# Last modified: 29/11/2021
# ===================================================

from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from ferias.models import Feria
from ferias.utils import is_in_radius
from api.serializers.feria_serializer import FeriaSerializer
from api.views.utils import DynamicFieldsViewMixin
from api.docs.params.parameters import optional_params
from api.docs.params.ferias import ferias_params


@extend_schema(
    summary="ferias/",
    tags=['Ferias'],
    parameters=optional_params+ferias_params,)
class FeriaList(DynamicFieldsViewMixin, generics.ListAPIView):
    '''
    Get a list with all the Ferias. Some of the query parameters
    are used to filter the list. For example if we need to get
    the Ferias given the `provincia` we put in the query the
    param: `?provincia=1`
    '''
    queryset = Feria.objects.all()
    serializer_class = FeriaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['provincia', 'canton', 'distrito',
                        'horarios__dia_inicio', 'horarios__dia_final',
                        'horarios__hora_inicio', 'horarios__hora_final']
    search_fields = ['nombre', 'provincia',
                     'canton', 'distrito', 'horarios__dia_inicio',
                     'horarios__dia_final']

    def get_queryset(self):
        feria_id_filtered = []
        ferias = Feria.objects.all()
        # Parametros del URL
        lat = self.request.query_params.get('lat')
        lon = self.request.query_params.get('lon')
        radius = self.request.query_params.get('radius')
        # Filtrar por latitud, longitud y radio
        if lat is not None and lon is not None and radius is not None:
            index = 0
            for feria in ferias.iterator():
                # Verificar si esta en el radio
                if is_in_radius(float(lat), float(lon),
                                 feria.latitud, feria.longitud,
                                 int(radius)):
                    # Agregar ID de la feria
                    feria_id_filtered.insert(index, feria.feria_id)
                    index = index + 1
            # Filtrar las ferias que esten es el radio dado
            return ferias.filter(feria_id__in=feria_id_filtered)
        else:
            # Devolver todas las ferias si falta alguno de los parametros
            return ferias


@extend_schema(
    summary="ferias/{feria_id}/",
    tags=['Ferias'],
    parameters=optional_params)
class FeriaDetail(DynamicFieldsViewMixin, generics.RetrieveAPIView):
    ''' Get a specific Feria by their ID (pk)'''
    queryset = Feria.objects.all()
    serializer_class = FeriaSerializer
