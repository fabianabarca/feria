# ===================================================
# Aqui guardaremos los paremetros genericos de cada
# la vista Ferias del API
#
# Author: Tyron Fonseca - tyron.fonseca@ucr.ac.cr
# Last modified: 02/12/2021
# ===================================================

from drf_spectacular.utils import OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes

# Parametros opcionales relacionadas a las Ferias

ferias_params = [
    OpenApiParameter(
        name='lat',
        location=OpenApiParameter.QUERY,
        description='Latitude of the user. Use with `lon` and `radius` to get '
        + 'all Fairs given the geolocation that the user pass.',
        required=False,
        type=OpenApiTypes.FLOAT
    ),
    OpenApiParameter(
        name='lon',
        location=OpenApiParameter.QUERY,
        description='Longitude of the user. Use with `lat` and `radius` to get'
        + ' all Fairs given the geolocation that the user pass.',
        required=False,
        type=OpenApiTypes.FLOAT
    ),
    OpenApiParameter(
        name='radius',
        location=OpenApiParameter.QUERY,
        description='Radius of the search in meters. Use with `lon` and `lat` '
        + 'to get all Fairs given the geolocation that the user pass.',
        required=False,
        type=OpenApiTypes.INT
    ),
    OpenApiParameter(
        name='search',
        location=OpenApiParameter.QUERY,
        description='Get a list of Ferias given the param. The search uses a '
        + '`LIKE` operator in the fields:\n* `nombre`\n* `provincia`\n* `canton`'
        + '\n* `distrito`\n* `horarios__dia_inicio`\n* `horarios__dia_final`',
        required=False,
        type=OpenApiTypes.STR,
        examples=[
            OpenApiExample(
                'Example 1: Search by ',
                summary='Value to search',
                description='Get a list of Ferias given the search.',
                value='Anything'
            ),
        ]
    )
]
