# ===================================================
# Aqui guardaremos los paremetros genericos de cada
# una de las vistas del API
#
# Author: Tyron Fonseca - tyron.fonseca@ucr.ac.cr
# Last modified: 02/12/2021
# ===================================================

from drf_spectacular.utils import OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes


# Parametros opcionales que se desplegaran en algunas vistas
optional_params = [
    OpenApiParameter(
        name='fields',
        location=OpenApiParameter.QUERY,
        description='Get specific fields that will be returned in the response',
        required=False,
        type=OpenApiTypes.STR,
        examples=[
            OpenApiExample(
                'Example 1: Get with only field Nombre',
                summary='Get the object with only the field Nombre',
                description='Get a response that only return the field Nombre',
                value='?fields=Nombre'
            ),
            OpenApiExample(
                'Example 2: Get specific fields',
                summary='Get the object with only the field specific fields',
                description='Get a response that only return the specific',
                value='?fields=Nombre,Descripcion,Id,...'
            )
        ]
    )
]

# Parametros opcionales de coordenadas relacionadas a las Ferias

coord_param = [
    OpenApiParameter(
        name='lat',
        location=OpenApiParameter.QUERY,
        description='Latitude of the user. Use with `lon` and `radius` to get '
        + 'Ferias given the geolocation that the user pass.',
        required=False,
        type=OpenApiTypes.FLOAT
    ),
    OpenApiParameter(
        name='lon',
        location=OpenApiParameter.QUERY,
        description='Longitude of the user. Use with `lat` and `radius` to get'
        + ' Ferias given the geolocation that the user pass.',
        required=False,
        type=OpenApiTypes.FLOAT
    ),
    OpenApiParameter(
        name='radius',
        location=OpenApiParameter.QUERY,
        description='Radius of the search in meters. Use with `lon` and `lat` '
        + 'to get Ferias given the geolocation that the user pass.',
        required=False,
        type=OpenApiTypes.INT
    ),
]

# Examples Ferias

examples_ferias = [
    OpenApiExample(
        name='Example Get Feria',
        description='Get a list of all Ferias',
        media_type='application/json',
        status_codes=['200']
    )
]
