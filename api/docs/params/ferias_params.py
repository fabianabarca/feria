# ===================================================
# Aqui guardaremos los paremetros genericos de cada
# la vista Ferias del API
#
# Last modified: 27/01/2022 - Tyron
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
        name='metodo_pago',
        location=OpenApiParameter.QUERY,
        description='Get a list of Ferias give the method of payment',
        required=False,
        type=OpenApiTypes.STR,
        examples=[
            OpenApiExample(
                'Example 1: OnlyCash',
                summary='Search Ferias that only accept cash as payment',
                description='',
                value='efectivo'
            ),
            OpenApiExample(
                'Example 2: OnlyCash + SINPE',
                summary='Search Ferias that only accept cash or SINPE as payment',
                description='',
                value='efectivo;SINPE'
            ),
            OpenApiExample(
                'Example 3: OnlyCash + SINPE + Debit/Credit card',
                summary='Search Ferias that only accept cash or SINPE or Debit/Credit card has payment',
                description='',
                value='efectivo;SINPE;tarjeta'
            ),
        ]
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
