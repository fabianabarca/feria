#Clase para tener funciones útiles que pueden ser utilizadas en el modelo y views

import math
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import ugettext as _


#Se busca que sea: +506<9 o 15 digitos>, ejemplo +50625242360
telefonoRegex = RegexValidator(regex=r"^\+?506?\d{9,15}$")

PROVINCIAS = (
    (0, 'San José'),
    (1, 'Alajuela'),
    (2, 'Cartago'),
    (3, 'Heredia'),
    (4, 'Guanacaste'),
    (5, 'Puntarenas'),
    (6, 'Limon')
)

DIAS_SEMANA = (
    ('L', 'Lunes'),
    ('K', 'Martes'),
    ('M', 'Miércoles'),
    ('J', 'Jueves'),
    ('V', 'Viernes'),
    ('S', 'Sábado')
)

CATEGORIAS_PRODUCTOS = (
    (0, 'Frutas'),
    (1, 'Vegetales'),
    (2, 'Lácteos'),
    (3, 'Artesanías'),
    (4, 'Comidas'),
    (5, 'Otros')
)

def is_in_radius(lat1, lon1, lat2, lon2, radius):
    """ Calcular distancia de dos coordenadas usando la formula Haversine
            https://www.movable-type.co.uk/scripts/latlong.html
        """

    radius_earth = 6371e3  # Radio de la tierra en metros
    pi_radian = (math.pi/180)
    phi_1 = lat1 * pi_radian
    phi_2 = lat2 * pi_radian
    delta_phi = (lat2 - lat1) * pi_radian
    delta_lambda = (lon2 - lon1) * pi_radian

    a = math.sin(delta_phi/2)**2 + math.cos(phi_1) * \
        math.cos(phi_2) * math.sin(delta_lambda/2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = radius_earth * c
    if distance <= radius:
        return True
    else:
        return False

def get_provincia_num(nombre):
    ''' Conseguir el numero de provincia segun el nombre '''
    inverse_dict = dict((v, k) for k, v in PROVINCIAS)
    prov = -1
    for k,v in inverse_dict.items():
        if nombre.lower() in k.lower():
            prov = v
            break
    return prov
