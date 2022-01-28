from drf_spectacular.utils import OpenApiExample

# Respuesta generica de horarios
generic_response_horarios = [{
    "dia_inicio": "L",
    "hora_inicio": "14:15:22Z",
    "dia_final": "L",
    "hora_final": "14:15:22Z"
}]


# Ejemplo de peticiones a Horarios
examples_horarios_list = [
    OpenApiExample(
        'Example 1',
        summary='Get a list all Horarios of a given Feria',
        description='Get all a list Horarios of a given Feria',
        request_only=False,
        response_only=True,
        value=generic_response_horarios
    )
]
