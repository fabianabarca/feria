import json
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from ferias.models import Producto


class ProductoTestCase(TestCase):
    def setUp(self):
        Producto.objects.create(
            categoria=0,
            nombre_cientifico='M. paradisiaca',
            nombre_comun='Banano',
            imagen='/producto/Banano/1630850814936.jpg',
            descripcion='Descripcion 1',
            temporada='Ene-Dic',
            precio=25.15
        )
        Producto.objects.create(
            categoria=4,
            nombre_cientifico='Frittata di spaguetti',
            nombre_comun='Torta de huevo con macarrones',
            imagen='/producto/Torta/image.jpg',
            descripcion='Descripcion 2',
            temporada='Mar-Ago',
            precio=14.13
        )

        self.frittada_expected_json = {
            "categoria": 4, "nombre_cientifico": "Frittata di spaguetti",
            "nombre_comun": "Torta de huevo con macarrones",
            "imagen": "http://testserver/media/producto/Torta/image.jpg",
            "descripcion": "Descripcion 2",
            "temporada": "Mar-Ago",
            "precio": 14.13
        }

    def test_get_productos(self):
        """Test get_productos"""

        # arrange
        client = APIClient()

        # act
        response = client.get('/api/productos/', format='json')
        result = json.loads(response.content)
        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(result), 2)

        for producto in result:
            self.assertIn('categoria', producto)
            self.assertIn('nombre_cientifico', producto)
            self.assertIn('nombre_comun', producto)
            self.assertIn('imagen', producto)
            self.assertIn('descripcion', producto)
            self.assertIn('temporada', producto)
            self.assertIn('precio', producto)

    def test_get_producto_by_id(self):
        """Test get_producto_by_id"""

        # arrange
        client = APIClient()

        # act
        response = client.get('/api/productos/1/', format='json')
        result = json.loads(response.content)
        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(result), 7)
        self.assertIn('categoria', result)
        self.assertIn('nombre_cientifico', result)
        self.assertIn('nombre_comun', result)
        self.assertIn('imagen', result)
        self.assertIn('descripcion', result)
        self.assertIn('temporada', result)
        self.assertIn('precio', result)

    def test_get_producto_by_id_invalid(self):
        """Test get_producto_by_id_invalid"""

        # arrange
        client = APIClient()

        # act
        response = client.get('/api/productos/14/', format='json')

        # assert
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_productos_specific_fields(self):
        """Test get_productos_specific_fields"""

        # arrange
        client = APIClient()
        url = '/api/productos/?fields=nombre_comun,categoria,descripcion'

        # act
        response = client.get(url, format='json')
        result = json.loads(response.content)

        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(result), 2)

        for producto in result:
            self.assertIn('categoria', producto)
            self.assertNotIn('nombre_cientifico', producto)
            self.assertIn('nombre_comun', producto)
            self.assertNotIn('imagen', producto)
            self.assertIn('descripcion', producto)
            self.assertNotIn('temporada', producto)
            self.assertNotIn('precio', producto)

    def test_get_productos_invalid_specific_fields(self):
        """Test get_productos_invalid_specific_fields"""

        # arrange
        client = APIClient()
        url = '/api/productos/?fields=dsads,dsad,dsf23'

        # act
        response = client.get(url, format='json')
        result = json.loads(response.content)

        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(result), 2)

        for producto in result:
            self.assertNotIn('categoria', producto)
            self.assertNotIn('nombre_cientifico', producto)
            self.assertNotIn('nombre_comun', producto)
            self.assertNotIn('imagen', producto)
            self.assertNotIn('descripcion', producto)
            self.assertNotIn('temporada', producto)
            self.assertNotIn('precio', producto)

    def test_get_productos_search(self):
        """Test get_productos_search"""

        # arrange
        client = APIClient()
        url = '/api/productos/?search=Descripcion 2&fields='

        # act
        response = client.get(url, format='json')
        result = json.loads(response.content)

        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], self.frittada_expected_json)

        for producto in result:
            self.assertIn('categoria', producto)
            self.assertIn('nombre_cientifico', producto)
            self.assertIn('nombre_comun', producto)
            self.assertIn('imagen', producto)
            self.assertIn('descripcion', producto)
            self.assertIn('temporada', producto)
            self.assertIn('precio', producto)

    def test_get_productos_search_invalid(self):
        """Test get_productos_search_invalid"""

        # arrange
        client = APIClient()
        url = '/api/productos/?search=sadasd'

        # act
        response = client.get(url, format='json')
        result = json.loads(response.content)

        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(result), 0)

    def test_get_productos_search_with_specific_fields(self):
        """Test get_productos_search_with_specific_fields"""

        # arrange
        client = APIClient()
        url = '/api/productos/?search=Descripcion 2&fields=imagen,categoria'

        # act
        response = client.get(url, format='json')
        result = json.loads(response.content)

        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(result), 1)

        for producto in result:
            self.assertIn('categoria', producto)
            self.assertNotIn('nombre_cientifico', producto)
            self.assertNotIn('nombre_comun', producto)
            self.assertIn('imagen', producto)
            self.assertNotIn('descripcion', producto)
            self.assertNotIn('temporada', producto)
            self.assertNotIn('precio', producto)

    def test_get_producto_by_specific_field(self):
        """Test get_producto_by_specific_field"""

        # arrange
        client = APIClient()
        url = '/api/productos/?temporada=Mar-Ago'

        # act
        response = client.get(url, format='json')
        result = json.loads(response.content)

        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], self.frittada_expected_json)

        for producto in result:
            self.assertIn('categoria', producto)
            self.assertIn('nombre_cientifico', producto)
            self.assertIn('nombre_comun', producto)
            self.assertIn('imagen', producto)
            self.assertIn('descripcion', producto)
            self.assertIn('temporada', producto)
            self.assertIn('precio', producto)

    def test_get_producto_by_specific_field_invalid(self):
        """Test get_producto_by_specific_field_invalid"""

        # arrange
        client = APIClient()
        url = '/api/productos/?temporada=asdsad'

        # act
        response = client.get(url, format='json')
        result = json.loads(response.content)

        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(result), 0)
