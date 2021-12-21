# Pruebas API (Unit Testing)

En este directorio se encuentran las pruebas de los metodos del API. Es necesario hacer esto ya que debemos garantizar el correcto funcionamiento del API ya que se espera que otros lo utilicen. Asi que antes de hacer merge con la rama `main` debemos asegurarnos que **todas las pruebas funcionan**.

Cuando se ejecutan las pruebas Django crea un servidor de prueba independiente al principal y además crea una base de datos temporal que se elimina cuando las pruebas finalizan. 

## Tabla de contenidos

1. [Ejecución](#ejecucion)
    1. [Ejecutar Todas](#ejecucion-todas)
    2. [Ejecutar una prueba especifica](#ejecucion-especifica)
2. [Crear pruebas](#crear)

<a name="ejecucion"></a>
## Ejecución 
Hay dos maneras de ejecutar las pruebas ya sea ejecutarlas todas o especificar cuales queremos ejecutar.

<a name="ejecucion-todas"></a>
### Ejecutar Todas

Para ejecutar todas nada mas debemos abrir la terminal y correr el siguiente comando:

```sh
py .\manage.py test 
```
Si usamos este comando se ejecutarán todas las pruebas del proyecto (web y api).

<a name="ejecucion-especifica"></a>
### Ejecutar una prueba especifica

Para ejecutar una prueba especifica debemos abrir la terminal y correr el siguiente comando:

```sh
py .\manage.py test api.test.<nombre_archivo_de_pruebas>
```

Por ejemplo si queremos ejecutar las pruebas de Ferias podemos el siguiente comando:
```sh
py .\manage.py test api.test.tests_ferias
```

<a name="crear"></a>
## Crear pruebas

Para crear pruebas hacemos uso de [Unittest], [Django Unit Testing], [Django REST Framework Unit Testing]. Basado en este [Tutorial] (en español) de [Alber].

1. Creamos un archivo que empiece con: ```tests_ejemplo.py```
2. Importamos las siguentes clases:
```
import json
from datetime import datetime
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
```
4. Creamos una clase que siga el formato camel case: 
 ```
 class EjemploTestCase(TestCase): 
 
 ```
Debe de tener al final **TestCase** para que sea reconocido.

5. Definimos el método/función que nos servirá para configurar cualquier parametro que necesitemos en las pruebas
 ```
 class EjemploTestCase(TestCase): 
     def setUp(self):
          # Definir parametros
 ```

Dentro de ese método/función podemos crear datos he ingresarlos a la base de datos temporal de pruebas. Por ejemplo:
```
class EjemploTestCase(TestCase):
    def setUp(self):
        Producto.objects.create(
            categoria=0,
            nombre_cientifico='M. paradisiaca',
            nombre_comun='Banano',
            imagen='/producto/Banano/1630850814936.jpg',
            descripcion='Descripcion 1',
            temporada='Ene-Dic'
        )
 ```
6. Después podemos definir cuantas pruebas queramos, las funciones/metodos deben seguir snake case (snake_case) y empezar siempre por ```test_```, esto se hace de la siguiente manera: 

 ```
 class EjemploTestCase(TestCase): 
     def setUp(self):
        Producto.objects.create(
            categoria=0,
            nombre_cientifico='M. paradisiaca',
            nombre_comun='Banano',
            imagen='/producto/Banano/1630850814936.jpg',
            descripcion='Descripcion 1',
            temporada='Ene-Dic'
        )
          
     def test_get_productos(self):
        """Test get_productos"""

        # arrange
        client = APIClient()

        # act
        response = client.get('/api/productos/', format='json')
        result = json.loads(response.content)
        
        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
 ```
- ```APIClient()``` Es nuestro API y con el podemos hacer las consultas que queramos.
- ```response``` Es la respuesta HTTP que el servidor nos da
- ```result``` Es el resultado de nuestra consulta en formato JSON
- ```self.assertEqual(param1, param2)``` Es donde hacemos la prueba, si ```param1``` y ```param2``` son iguales la prueba funciona, en caso contrario la prueba nos dará error.


[Unittest]: https://docs.python.org/3/library/unittest.html
[Django Unit Testing]: https://docs.djangoproject.com/en/3.2/internals/contributing/writing-code/unit-tests/
[Django REST Framework Unit Testing]: https://www.django-rest-framework.org/api-guide/testing/
[Tutorial]: https://web.archive.org/web/20210417151056/https://cosasdedevs.com/posts/unittest-con-django-rest-fraework/
[Alber]: https://github.com/albertorc87