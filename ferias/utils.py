#Clase para tener funciones útiles que pueden ser utilizadas en el modelo y views

import math
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import ugettext as _


#Se busca que sea: +506<9 o 15 digitos>, ejemplo +50625242360
telefonoRegex = RegexValidator(regex=r"^\+?506?\d{9,15}$")

DAY_OF_THE_WEEK = {
    '1': _(u'Lunes'),
    '2': _(u'Martes'),
    '3': _(u'Miércoles'),
    '4': _(u'Jueves'),
    '5': _(u'Viernes'),
    '6': _(u'Sábado'),
    '7': _(u'Domingo'),
}

#Creamos un campo especial para el día de la semana
class DayOfTheWeekField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['choices'] = tuple(sorted(DAY_OF_THE_WEEK.items()))
        kwargs['max_length'] = 1
        super(DayOfTheWeekField, self).__init__(*args, **kwargs)


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
