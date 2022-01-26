from django import forms
from ferias.models import Feria, Horario, Producto, Foto

''' Acá se crean los forms básicos para el manejo de los modelos '''


class FeriaForm(forms.ModelForm):
    ferias_id = forms.CharField(
        required=True,
        help_text="Introduzca 3 caracteres que representen esta feria. Ej: "
                  " Feria de San Carlos = SCA")

    class Meta:
        model = Feria
        fields = '__all__'


class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = '__all__'


class ProductoForm(forms.ModelForm):
    temporada = forms.CharField(
        required=False,
        help_text="Indique el rango de meses en los que este producto se "
                  "encuentra en temporada. Ej: Feb-Abr")

    class Meta:
        model = Producto
        fields = '__all__'


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Foto
        fields = '__all__'
