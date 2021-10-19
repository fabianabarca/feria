from django.contrib import admin
from .models import *


class FeriaAdmin(admin.ModelAdmin):
    filter_horizontal = ('productos','vendedores','telefonos',)

admin.site.register(Feria, FeriaAdmin)
admin.site.register(Vendedor)
admin.site.register(Telefono)
admin.site.register(Producto)
