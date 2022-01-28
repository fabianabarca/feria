# ===================================================
# Aqui guardaremos los paremetros genericos de cada
# una de las vistas del API
#
# Last modified: 27/01/2022 - Tyron
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
                summary='Get the object with only the specific fields',
                description='Get a response that only return the specific',
                value='?fields=Nombre,Descripcion,Id,...'
            )
        ]
    )
]
