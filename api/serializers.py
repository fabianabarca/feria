#Clase encargada de serializar y deserializar las instancias de los modelos de las ferias.
#
from rest_framework import serializers
from ferias.models import Producto, Feria

class ProductoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nombre_cientifico = serializers.CharField(max_length=128, allow_blank=True)
    nombre_comun = serializers.CharField(max_length=128)
    descripcion = serializers.CharField()
    temporada = serializers.CharField()
    categoria = serializers.IntegerField(max_value=5, min_value=0)
    imagen = serializers.ImageField(allow_empty_file=True)
    icono = serializers.ImageField(allow_empty_file=True)

    def create(self, validate_data):
        """
        Crear y retornar una instancia de Producto, con las validaciones
        """
        return Producto.objects.create(**validate_data)

    def update(self, instance, validate_data):
        """
        Actualizar y retornar una instancia de Producto, con las validaciones
        """
        instance.categoria = validate_data.get('categoria', instance.categoria)
        instance.nombre_cientifico = validate_data.get('nombre_cientifico', instance.nombre_cientifico)
        instance.nombre_comun = validate_data.get('nombre_comun', instance.nombre_comun)
        instance.descripcion = validate_data.get('descripcion', instance.descripcion)
        instance.temporada = validate_data.get('temporada', instance.temporada)
        instance.imagen = validate_data.get('imagen', instance.imagen)
        instance.icono = validate_data.get('icono', instance.icono)
        instance.save()
        return instance


class FeriaSerializer(serializers.Serializer):
    ferias_id = serializers.CharField(max_length=3)
    codigo = serializers.CharField(max_length=30)
    nombre = serializers.CharField(max_length=128)
    provincia = serializers.IntegerField(max_value=6, min_value=0)
    canton = serializers.CharField(max_length=128)
    distrito = serializers.CharField(max_length=128)
    direccion = serializers.CharField()
    latitud = serializers.FloatField()
    longitud = serializers.FloatField()
    oferta = ProductoSerializer(read_only=True, many=True)

    def create(self, validate_data):
        """
        Crear y retornar una instancia de Feria, con las validaciones
        """
        return Producto.objects.create(**validate_data)

    def update(self, instance, validate_data):
        """
        Actualizar y retornar una instancia de Feria, con las validaciones
        """
        instance.codigo = validate_data.get('codigo', instance.codigo)
        instance.nombre = validate_data.get('nombre', instance.nombre)
        instance.provincia = validate_data.get('provincia', instance.provincia)
        instance.canton = validate_data.get('canton', instance.canton)
        instance.distrito = validate_data.get('distrito', instance.distrito)
        instance.direccion = validate_data.get('direccion', instance.direccion)
        instance.latitud = validate_data.get('latitud', instance.latitud)
        instance.longitud = validate_data.get('longitud', instance.longitud)
        instance.save()
        return instance
