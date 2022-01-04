# ===================================================
# Clases encargadas que ayudan a las vistas
#
# Author: Tyron Fonseca - tyron.fonseca@ucr.ac.cr
# Last modified: 4/1/2022
# ===================================================

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
