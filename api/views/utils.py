# ===================================================
# Clases encargadas que ayudan a las vistas
#
# Author: Tyron Fonseca - tyron.fonseca@ucr.ac.cr
# Last modified: 24/11/2021
# ===================================================

import math


class FeriasHelper:
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


class DynamicFieldsViewMixin(object):
    """
    Esta clase nos permite escojer los campos (fields) que queramos
    que el API nos devuelva, agregando un parametro ('field') con los
    campos que queremos que se devuelvan.
    Tomado de: https://stackoverflow.com/a/31979444/6156666
    """
    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        fields = None
        if self.request.method == 'GET':
            query_fields = self.request.query_params.get("fields", None)
            if query_fields:
                fields = tuple(query_fields.split(','))

        kwargs['context'] = self.get_serializer_context()
        kwargs['fields'] = fields

        return serializer_class(*args, **kwargs)
