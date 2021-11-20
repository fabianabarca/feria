# ===================================================
# Clases encargadas que ayudan a los serializadores
#
# Author: Tyron Fonseca - tyron.fonseca@ucr.ac.cr
# Last modified: 20/11/2021
# ===================================================


class DynamicFieldsSerializerMixin(object):
    """
    Esta clase nos permite escojer los campos (fields) que queramos
    que el API nos devuelva, modificando el serializador.
    Tomado de: https://stackoverflow.com/a/31979444/6156666
    """
    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super(DynamicFieldsSerializerMixin, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)
