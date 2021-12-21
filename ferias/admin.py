from django.contrib import admin
from ferias.models import Feria, Horario, Producto
from ferias.forms import FeriaForm, HorarioForm, ProductoForm


class FeriaAdmin(admin.ModelAdmin):
    search_fields = ['ferias_id', 'nombre', 'distrito']
    list_display = ('ferias_id', '__str__', 'provincia')
    list_filter = ['provincia', 'canton']
    filter_horizontal = ('oferta',)
    form = FeriaForm


class HorarioAdmin(admin.ModelAdmin):
    search_fields = ['feria']
    list_filter = ['dia_inicio', 'dia_final']
    form = HorarioForm


class ProductoAdmin(admin.ModelAdmin):
    search_fields = ['nombre_comun', 'nombre_cientifico']
    list_filter = ['categoria']
    form = ProductoForm


admin.site.register(Feria, FeriaAdmin)
admin.site.register(Horario, HorarioAdmin)
admin.site.register(Producto, ProductoAdmin)
