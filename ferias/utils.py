#Clase para tener funciones útiles que pueden ser utilizadas en el modelo y views
#Creado por: Tyron Fonseca A. tyron.fonseca@ucr.ac.cr
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
