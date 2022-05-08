# ===================================================
# Aqui se realizan todas las pruebas de unidada
# relacionadas con el modelo Feria
#
# Last modified: 27/01/2022 - Tyron
# ===================================================

import json
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from ferias.models import Feria


class FeriaTestCase(TestCase):
    def setUp(self):
        Feria.objects.create(
            feria_id='SCA',
            codigo_url='San Carlos',
            nombre='Feria de San Carlos',
            provincia=1,
            canton='San Carlos',
            distrito='San Carlitos',
            direccion='Direccion 2',
            latitud=25.26526,
            longitud=-25.26526,            
            administrador='Admin1',
            conocida_como='Apodo',
            comite='comite1',
            telefono='12345679',
            metodo_pago='efectivo',
            estacionamiento=True,
            parqueo_bicicleta=True,
            sanitarios=True,
            campo_ferial=True,
            bajo_techo=True,
            agua_potable=True,
            accesibilidad=True
        )
        Feria.objects.create(
            feria_id='GUA',
            codigo_url='guadalupe',
            nombre='Feria de Guadalupe',
            provincia=0,
            canton='Goicoechea',
            distrito='Guadalupe',
            direccion='Direccion 1',
            latitud=9.947848,
            longitud=-84.055687,
            administrador='',
            conocida_como='Mercado libre de Guadalupe',
            comite='',
            telefono='',
            metodo_pago='Efectivo; SINPE',
            estacionamiento=False,
            parqueo_bicicleta=False,
            sanitarios=True,
            campo_ferial=False,
            bajo_techo=True,
            agua_potable=True,
            accesibilidad=False
        )

    def test_get_ferias(self):
        """Test get_ferias"""

        # arrange
        client = APIClient()

        # act
        response = client.get('/api/ferias/', format='json')
        result = json.loads(response.content)
        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(result), 2)

        for feria in result:
            self.assertIn('feria_id', feria)
            self.assertIn('oferta', feria)
            self.assertIn('horarios', feria)
            self.assertIn('nombre', feria)
            self.assertIn('codigo_url', feria)
            self.assertIn('provincia', feria)
            self.assertIn('canton', feria)
            self.assertIn('distrito', feria)
            self.assertIn('direccion', feria)
            self.assertIn('latitud', feria)
            self.assertIn('longitud', feria)
            self.assertIn('conocida_como', feria)
            self.assertIn('comite', feria)
            self.assertIn('administrador', feria)
            self.assertIn('metodo_pago', feria)
            self.assertIn('estacionamiento', feria)
            self.assertIn('parqueo_bicicleta', feria)
            self.assertIn('sanitarios', feria)
            self.assertIn('campo_ferial', feria)
            self.assertIn('bajo_techo', feria)
            self.assertIn('agua_potable', feria)
            self.assertIn('accesibilidad', feria)

    def test_get_feria_by_id(self):
        """Test get_ferias_by_id"""

        # arrange
        client = APIClient()

        # act
        response = client.get('/api/ferias/GUA/', format='json')
        result = json.loads(response.content)

        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(result), 23)

        self.assertIn('feria_id', result)
        self.assertIn('oferta', result)
        self.assertIn('horarios', result)
        self.assertIn('nombre', result)
        self.assertIn('codigo_url', result)
        self.assertIn('provincia', result)
        self.assertIn('canton', result)
        self.assertIn('distrito', result)
        self.assertIn('direccion', result)
        self.assertIn('latitud', result)
        self.assertIn('longitud', result)

    def test_get_feria_by_search_term(self):
        """Test get_ferias_by_seach_term"""

        # arrange
        client = APIClient()

        # act
        response = client.get('/api/ferias/?search=guada', format='json')
        result = json.loads(response.content)

        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(result), 1)

        self.assertIn('feria_id', result[0])
        self.assertIn('oferta', result[0])
        self.assertIn('horarios', result[0])
        self.assertIn('nombre', result[0])
        self.assertIn('codigo_url', result[0])
        self.assertIn('provincia', result[0])
        self.assertIn('canton', result[0])
        self.assertIn('distrito', result[0])
        self.assertIn('direccion', result[0])
        self.assertIn('latitud', result[0])
        self.assertIn('longitud', result[0])
        self.assertIn('conocida_como', result[0])
        self.assertIn('comite', result[0])
        self.assertIn('administrador', result[0])
        self.assertIn('metodo_pago', result[0])
        self.assertIn('estacionamiento', result[0])
        self.assertIn('parqueo_bicicleta', result[0])
        self.assertIn('sanitarios', result[0])
        self.assertIn('campo_ferial', result[0])
        self.assertIn('bajo_techo', result[0])
        self.assertIn('agua_potable', result[0])
        self.assertIn('accesibilidad', result[0])

    def test_get_feria_by_specific_field(self):
        """Test get_ferias_by_specific_field"""

        # arrange
        client = APIClient()

        # act
        response = client.get('/api/ferias/?provincia=0', format='json')
        result = json.loads(response.content)

        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(result), 1)

        self.assertIn('feria_id', result[0])
        self.assertIn('oferta', result[0])
        self.assertIn('horarios', result[0])
        self.assertIn('nombre', result[0])
        self.assertIn('codigo_url', result[0])
        self.assertIn('provincia', result[0])
        self.assertIn('canton', result[0])
        self.assertIn('distrito', result[0])
        self.assertIn('direccion', result[0])
        self.assertIn('latitud', result[0])
        self.assertIn('longitud', result[0])
        self.assertIn('conocida_como', result[0])
        self.assertIn('comite', result[0])
        self.assertIn('administrador', result[0])
        self.assertIn('metodo_pago', result[0])
        self.assertIn('estacionamiento', result[0])
        self.assertIn('parqueo_bicicleta', result[0])
        self.assertIn('sanitarios', result[0])
        self.assertIn('campo_ferial', result[0])
        self.assertIn('bajo_techo', result[0])
        self.assertIn('agua_potable', result[0])
        self.assertIn('accesibilidad', result[0])

    def test_get_feria_by_specific_field_invalid(self):
        """Test get_ferias_by_specific_invalid"""

        # arrange
        client = APIClient()

        # act
        response = client.get('/api/ferias/?provincia=3', format='json')
        result = json.loads(response.content)

        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(result), 0)

    def test_get_feria_by_search_term_invalid(self):
        """Test get_feria_by_search_term_invalid"""

        # arrange
        client = APIClient()

        # act
        response = client.get('/api/ferias/?search=asdsaf', format='json')
        result = json.loads(response.content)

        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(result), 0)

    def test_get_feria_not_found(self):
        """Test get_feria_not_found"""

        # arrange
        client = APIClient()

        # act
        response = client.get('/api/ferias/sdasd/', format='json')

        # assert
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_feria_by_geolocation(self):
        """Test get_feria_by_geolocation"""

        # arrange
        client = APIClient()
        url = '/api/ferias/?lat=9.95190399&lon=-84.04507004&radius=2000'

        # act
        response = client.get(url, format='json')
        result = json.loads(response.content)

        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(result), 1)

        for feria in result:
            self.assertIn('feria_id', feria)
            self.assertIn('oferta', feria)
            self.assertIn('horarios', feria)
            self.assertIn('nombre', feria)
            self.assertIn('codigo_url', feria)
            self.assertIn('provincia', feria)
            self.assertIn('canton', feria)
            self.assertIn('distrito', feria)
            self.assertIn('direccion', feria)
            self.assertIn('latitud', feria)
            self.assertIn('longitud', feria)
            self.assertIn('conocida_como', feria)
            self.assertIn('comite', feria)
            self.assertIn('administrador', feria)
            self.assertIn('metodo_pago', feria)
            self.assertIn('estacionamiento', feria)
            self.assertIn('parqueo_bicicleta', feria)
            self.assertIn('sanitarios', feria)
            self.assertIn('campo_ferial', feria)
            self.assertIn('bajo_techo', feria)
            self.assertIn('agua_potable', feria)
            self.assertIn('accesibilidad', feria)

    def test_get_feria_by_geolocation_invalid(self):
        """Test get_feria_by_geolocation_invalid"""

        # arrange
        client = APIClient()
        url = '/api/ferias/?lat=9.95190399&lon=-84.04507004'

        # act
        response = client.get(url, format='json')
        result = json.loads(response.content)

        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(result), 2)

    def test_get_feria_by_geolocation_tiny_radius(self):
        """Test get_feria_by_geolocation_tiny_radius"""

        # arrange
        client = APIClient()
        url = '/api/ferias/?lat=9.95190399&lon=-84.04507004&radius=1'

        # act
        response = client.get(url, format='json')
        result = json.loads(response.content)

        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(result), 0)

    def test_get_feria_by_geolocation_negative_radius(self):
        """Test get_feria_by_geolocation_negative_radius"""

        # arrange
        client = APIClient()
        url = '/api/ferias/?lat=9.95190399&lon=-84.04507004&radius=-100'

        # act
        response = client.get(url, format='json')
        result = json.loads(response.content)

        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(result), 0)

    def test_get_feria_by_geolocation_far_coords(self):
        """Test get_feria_by_geolocation_far_coords"""

        # arrange
        client = APIClient()
        url = '/api/ferias/?lat=19.95190399&lon=84.04507004&radius=10000'

        # act
        response = client.get(url, format='json')
        result = json.loads(response.content)

        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(result), 0)

    def test_get_ferias_specific_fields(self):
        """Test get_ferias_specific_fields"""

        # arrange
        client = APIClient()
        url = '/api/ferias/?fields=latitud,longitud'

        # act
        response = client.get(url, format='json')
        result = json.loads(response.content)

        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(result), 2)

        for feria in result:
            self.assertNotIn('feria_id', feria)
            self.assertNotIn('oferta', feria)
            self.assertNotIn('horarios', feria)
            self.assertNotIn('nombre', feria)
            self.assertNotIn('codigo_url', feria)
            self.assertNotIn('provincia', feria)
            self.assertNotIn('canton', feria)
            self.assertNotIn('distrito', feria)
            self.assertNotIn('direccion', feria)
            self.assertIn('latitud', feria)
            self.assertIn('longitud', feria)
            self.assertNotIn('conocida_como', feria)
            self.assertNotIn('comite', feria)
            self.assertNotIn('administrador', feria)
            self.assertNotIn('metodo_pago', feria)
            self.assertNotIn('estacionamiento', feria)
            self.assertNotIn('parqueo_bicicleta', feria)
            self.assertNotIn('sanitarios', feria)
            self.assertNotIn('campo_ferial', feria)
            self.assertNotIn('bajo_techo', feria)
            self.assertNotIn('agua_potable', feria)
            self.assertNotIn('accesibilidad', feria)

    def test_get_ferias_invalid_specific_fields(self):
        """Test get_ferias_invalid_specific_fields"""

        # arrange
        client = APIClient()
        url = '/api/ferias/?fields=comida,perro,'

        # act
        response = client.get(url, format='json')
        result = json.loads(response.content)

        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(result), 2)

        for feria in result:
            self.assertNotIn('feria_id', feria)
            self.assertNotIn('oferta', feria)
            self.assertNotIn('horarios', feria)
            self.assertNotIn('nombre', feria)
            self.assertNotIn('codigo_url', feria)
            self.assertNotIn('provincia', feria)
            self.assertNotIn('canton', feria)
            self.assertNotIn('distrito', feria)
            self.assertNotIn('direccion', feria)
            self.assertNotIn('latitud', feria)
            self.assertNotIn('longitud', feria)
            self.assertNotIn('conocida_como', feria)
            self.assertNotIn('comite', feria)
            self.assertNotIn('administrador', feria)
            self.assertNotIn('metodo_pago', feria)
            self.assertNotIn('estacionamiento', feria)
            self.assertNotIn('parqueo_bicicleta', feria)
            self.assertNotIn('sanitarios', feria)
            self.assertNotIn('campo_ferial', feria)
            self.assertNotIn('bajo_techo', feria)
            self.assertNotIn('agua_potable', feria)
            self.assertNotIn('accesibilidad', feria)

    def test_get_ferias_specific_fields_and_search(self):
        """Test get_ferias_specific_fields_and_search"""

        # arrange
        client = APIClient()
        url = '/api/ferias/?fields=latitud,longitud&search=guada'

        # act
        response = client.get(url, format='json')
        result = json.loads(response.content)

        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(result), 1)

        for feria in result:
            self.assertNotIn('feria_id', feria)
            self.assertNotIn('oferta', feria)
            self.assertNotIn('horarios', feria)
            self.assertNotIn('nombre', feria)
            self.assertNotIn('codigo_url', feria)
            self.assertNotIn('provincia', feria)
            self.assertNotIn('canton', feria)
            self.assertNotIn('distrito', feria)
            self.assertNotIn('direccion', feria)
            self.assertIn('latitud', feria)
            self.assertIn('longitud', feria)
            self.assertNotIn('conocida_como', feria)
            self.assertNotIn('comite', feria)
            self.assertNotIn('administrador', feria)
            self.assertNotIn('metodo_pago', feria)
            self.assertNotIn('estacionamiento', feria)
            self.assertNotIn('parqueo_bicicleta', feria)
            self.assertNotIn('sanitarios', feria)
            self.assertNotIn('campo_ferial', feria)
            self.assertNotIn('bajo_techo', feria)
            self.assertNotIn('agua_potable', feria)
            self.assertNotIn('accesibilidad', feria)
