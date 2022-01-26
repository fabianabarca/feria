from django.contrib import admin
from ferias.models import Feria, Horario, Producto, Foto
from ferias.forms import FeriaForm, HorarioForm, ProductoForm, FotoForm


class FeriaAdmin(admin.ModelAdmin):
    search_fields = ['feria_id', 'nombre', 'distrito']
    list_display = ('feria_id', '__str__', 'provincia')
    list_filter = ['provincia', 'canton']
    filter_horizontal = ('oferta',)
    form = FeriaForm


class HorarioAdmin(admin.ModelAdmin):
    search_fields = ['feria__nombre']
    list_filter = ['dia_inicio', 'dia_final']
    form = HorarioForm


class ProductoAdmin(admin.ModelAdmin):
    search_fields = ['nombre_comun', 'nombre_cientifico']
    list_filter = ['categoria']
    form = ProductoForm


class FotoAdmin(admin.ModelAdmin):
    search_fields = ['feria__nombre']
    list_filter = ('perfil', 'portada',)
    form = FotoForm


admin.site.register(Feria, FeriaAdmin)
admin.site.register(Horario, HorarioAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Foto, FotoAdmin)
