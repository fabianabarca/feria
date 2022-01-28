# ===================================================
# Aqui guardaremos los paremetros genericos de cada
# la vista Horarios del API
#
# Last modified: 27/01/2022 - Tyron
# ===================================================

from drf_spectacular.utils import OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes

# Parametros opcionales relacionadas a los Horarios

horarios_params = [
    OpenApiParameter(
        name='id',
        location=OpenApiParameter.QUERY,
        description='Id of the Feria to get the hours',
        required=True,
        type=OpenApiTypes.STR,
        examples=[
            OpenApiExample(
                'Example 1: ',
                summary='Id Feria',
                description='Get a list of the fair hours of given Feria.',
                value='SCR'
            ),
        ]
    )
]
