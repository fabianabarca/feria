# ===================================================
# Aqui guardaremos los paremetros genericos de cada
# la vista Productos del API
#
# Last modified: 27/01/2022 - Tyron
# ===================================================

from drf_spectacular.utils import OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes

# Parametros opcionales relacionadas a los Productos

productos_params = [
    OpenApiParameter(
        name='search',
        location=OpenApiParameter.QUERY,
        description='Get a list of Productos given the param. The search uses a '
        + '`LIKE` operator in the fields:\n* `nombre_cientifico`'
        + '\n* `nombre_comun`\n* `temporada`\n* `categoria`\n* `descripcion`',
        required=False,
        type=OpenApiTypes.STR,
        examples=[
            OpenApiExample(
                'Example 1: Search by ',
                summary='Value to search',
                description='Get a list of Productos given the search.',
                value='Anything'
            ),
        ]
    )
]
