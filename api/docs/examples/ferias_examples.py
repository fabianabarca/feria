from drf_spectacular.utils import OpenApiExample
# from typing_extensions import Literal

# Respuesta generica de ferias
generic_response_feria = [{
    "feria_id": "str",
    "oferta":
    [
        {
            "categoria": 0,
            "nombre_cientifico": "string",
            "nombre_comun": "string",
            "imagen": "http://example.com",
            "descripcion": "string",
            "temporada": "string"
        }
    ],
    "horarios":
    [
        {
            "dia_inicio": "L",
            "hora_inicio": "14:15:22Z",
            "dia_final": "L",
            "hora_final": "14:15:22Z"
        }
    ],
    "codigo_url": "string",
    "nombre": "string",
    "conocida_como": "string",
    "comite": "string",
    "administrador": "string",
    "telefono": "string",
    "provincia": 0,
    "canton": "string",
    "distrito": "string",
    "direccion": "string",
    "latitud": 0,
    "longitud": 0,
    "metodo_pago": "string",
    "estacionamiento":  True,
    "parqueo_bicicleta":  True,
    "sanitarios": True,
    "campo_ferial":  True,
    "bajo_techo": True,
    "agua_potable": True,
    "accesibilidad": True
}]


# Ejemplo de peticiones a Ferias List
examples_ferias_list = [
    OpenApiExample(
        'Example 1',
        summary='Get all Ferias',
        description='Get all the ferias with all the fields',
        request_only=False,
        response_only=True,
        value=generic_response_feria
    ),
    OpenApiExample(
        'Example 2',
        summary='Get all ferias with specific fields',
        description='Query params: *?fields=feria_id,codigo_url,nombre*',
        response_only=True,
        value=[{
            "feria_id": "str",
            "codigo_url": "string",
            "nombre": "string"
        }]
    ),
    OpenApiExample(
        'Example 3',
        summary='Get all ferias given the coords and radius',
        description='For this to work the three params: `lat`, `lon` and '
        + '`radius` needs to be in the query params. Eg. *?lon=10.2&lat=-'
        + '23.3&radius=200*',
        response_only=True,
        value=generic_response_feria
    ),
]
