''' Acá se crean los modelos base de las Ferias, junto con toda la información
    relevante de ellas '''

import datetime
import locale
from django.db import models
from django.utils.text import slugify

locale.setlocale(locale.LC_TIME, '')

''' Acá se crean los modelos base de las Ferias, junto con toda la información
    relevante de ellas '''

PROVINCIAS = (
    (0, 'San José'),
    (1, 'Alajuela'),
    (2, 'Cartago'),
    (3, 'Heredia'),
    (4, 'Guanacaste'),
    (5, 'Puntarenas'),
    (6, 'Limon')
)

DIAS_SEMANA = (
    ('L', 'Lunes'),
    ('K', 'Martes'),
    ('M', 'Miércoles'),
    ('J', 'Jueves'),
    ('V', 'Viernes'),
    ('S', 'Sábado')
)

CATEGORIAS_PRODUCTOS = (
    (0, 'Frutas'),
    (1, 'Vegetales'),
    (2, 'Lácteos'),
    (3, 'Artesanías'),
    (4, 'Comidas'),
    (5, 'Otros')
)

def path_producto(instance, filename):
    return 'producto/{}/{}'.format(instance.nombre_comun, filename)

class Producto(models.Model):
    ''' Modelo de un producto, contiene información básica de los diferentes
        productos que se pueden encontrar en las ferias '''

    categoria = models.PositiveSmallIntegerField(
        choices=CATEGORIAS_PRODUCTOS)
    nombre_cientifico = models.CharField(max_length=128, blank=True)
    nombre_comun = models.CharField(max_length=128)
    imagen = models.ImageField(upload_to=path_producto)
    icono = models.ImageField(upload_to=path_producto)
    descripcion = models.TextField()
    temporada = models.TextField()

    class Meta:
        managed = True
        db_table = 'productos'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.nombre_comun


class Feria(models.Model):
    ''' Modelo principal que contiene la información de las ferias del
        agricultor a nivel nacional '''

    ferias_id = models.CharField(max_length=3, primary_key=True)
    codigo = models.CharField(max_length=30)
    nombre = models.CharField(max_length=128)
    provincia = models.PositiveSmallIntegerField(choices=PROVINCIAS)
    canton = models.CharField(max_length=128)
    distrito = models.CharField(max_length=128)
    direccion = models.TextField()
    latitud = models.FloatField()
    longitud = models.FloatField()
    oferta = models.ManyToManyField(Producto, blank=True)

    class Meta:
        managed = True
        db_table = 'ferias'
        verbose_name = 'Feria del Agricultor'
        verbose_name_plural = 'Ferias del Agricultor'
        ordering = ['nombre']
    
    def get_slug(self):
        ''' Usamos esta funcion para conseguir el slug ya que 
        no se permiten caracteres que no sean ASCII '''
        return slugify(self.codigo)

    def abre_hoy(self):
        ''' Verifica si la feria abre hoy (hora server) '''
        abre = False
        dia = datetime.datetime.now().strftime("%A")[0]        
        for horario in self.horarios.all():
            if dia.lower() == horario.dia_inicio[0].lower():
                abre = True
                break
        return abre            

    def __str__(self):
        return self.nombre + ", " + self.distrito


class Horario(models.Model):
    ''' Horarios de las diferentes ferias, relaciona un miembro del modelo
        Ferias con un día y hora de inicio y un día y hora final '''

    feria = models.ForeignKey(to=Feria, related_name="horarios",
                              on_delete=models.DO_NOTHING)
    dia_inicio = models.CharField(max_length=1, choices=DIAS_SEMANA)
    hora_inicio = models.TimeField()
    dia_final = models.CharField(max_length=1, choices=DIAS_SEMANA)
    hora_final = models.TimeField()

    class Meta:
        managed = True
        db_table = 'horarios'
        verbose_name = 'Horario'
        verbose_name_plural = 'Horarios'

    def __str__(self):
        return (self.feria.nombre
                + " (" + self.dia_inicio + " - " + self.dia_final + ")")
