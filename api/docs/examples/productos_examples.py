from drf_spectacular.utils import OpenApiExample

# Respuesta generica de productos
generic_response_productos = [{
    "categoria": 0,
    "nombre_cientifico": "string",
    "nombre_comun": "string",
    "imagen": "http://example.com",
    "descripcion": "string",
    "temporada": "string",
    "precio": 1500.0
}]


# Ejemplo de peticiones a Productos List
examples_productos_list = [
    OpenApiExample(
        'Example 1',
        summary='Get all Productos',
        description='Get all the ferias with all the fields',
        request_only=False,
        response_only=True,
        value=generic_response_productos
    ),
    OpenApiExample(
        'Example 2',
        summary='Get all productos with specific fields',
        description='Query params: *?fields=categoria,nombre_cientifico*',
        response_only=True,
        value=[{
            "categoria": 0,
            "nombre_cientifico": "string"
        }]
    ),
]
