# Configuraciones del API

# Referencia: https://drf-spectacular.readthedocs.io/en/latest/settings.html
DRF_CONFIG = {
    'TITLE': 'Ferias CR API',
    'DESCRIPTION': 'API of the website Ferias CR',
    'VERSION': '0.0.1',
    'TOS': 'https: //localhost:8000/policies/terms/',
    'CONTACT': {
        'name': 'Fabian Abarca',
        'email': 'fabian.abarca@ucr.ac.cr',
        'url': '/api/doc/redoc'
    },
    'LICENSE': {
        'name': 'MIT',
        'url': 'https: //github.com/fabianabarca/ferias/blob/main/LICENSE'
    },
    # Permitir uso de regex
    'PREPROCESSING_HOOKS': [
        'drf_spectacular.hooks.preprocess_exclude_path_format'
    ],
    # Sobre escribir Enums que se pueden repetir
    'ENUM_NAME_OVERRIDES': {
        'DiaFinalEnum': 'ferias.models.DIAS_SEMANA',
    },
    # Quitar prefijo
    'SCHEMA_PATH_PREFIX': '/api/',
    # Esconder link o referencia a documento
    'SERVE_INCLUDE_SCHEMA': False,
    # Configuraciones extra
    # https://swagger.io/docs/specification/openapi-extensions/
    'EXTENSIONS_INFO': {
        "x-logo": {
            "url": "https://raw.githubusercontent.com/Redocly/redoc/master/docs/images/redoc.png",
            "backgroundColor": "#FFFFFF",
            "altText": "Example logo"
        }
    },
    # Secciones
    # Las descripciones permiten usar CommonMark https://commonmark.org/help/
    'TAGS': [
        {
            'name': 'About',
            'description': 'This API was developed by students of the TCU-691'
                           + ' "Tropicalización de la Tecnología".\n It uses '
                           + '[**OpenAPI version 3.0.3**](https://swagger.io/'
                           + 'specification/)'
        },
        {
            'name': 'Ferias',
            'description': 'Get data related to Ferias.'

        },
        {
            'name': 'Horarios',
            'description': 'Get data related to Horarios'
        },
        {
            'name': 'Productos',
            'description': 'Get data related to Productos'
        },
    ],
}
