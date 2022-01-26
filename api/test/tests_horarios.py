import json
from datetime import datetime
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from ferias.models import Feria, Horario


class FeriaTestCase(TestCase):
    def setUp(self):
        feria_sca = Feria.objects.create(
            feria_id='SCA',
            codigo='San Carlos',
            nombre='Feria de San Carlos',
            provincia=1,
            canton='San Carlos',
            distrito='San Carlitos',
            direccion='Direccion 2',
            latitud=25.26526,
            longitud=-25.26526
        )
        Horario.objects.create(
            feria=feria_sca,
            dia_inicio='L',
            hora_inicio=datetime.strptime('12:12:12', '%H:%M:%S').time(),
            dia_final='L',
            hora_final=datetime.strptime('16:16:16', '%H:%M:%S').time()
        )
        Horario.objects.create(
            feria=feria_sca,
            dia_inicio='K',
            hora_inicio=datetime.strptime('13:13:13', '%H:%M:%S').time(),
            dia_final='K',
            hora_final=datetime.strptime('17:17:17', '%H:%M:%S').time()
        )

        self.horario_0_expected_json = {
            "dia_inicio": "L",
            "hora_inicio": "12:12:12",
            "dia_final": "L",
            "hora_final": "16:16:16"
        }

        self.horario_1_expected_json = {
            "dia_inicio": "K",
            "hora_inicio": "13:13:13",
            "dia_final": "K",
            "hora_final": "17:17:17"
        }

    def test_get_horarios_by_id_feria(self):
        """Test get_horarios_by_id_feria"""

        # arrange
        client = APIClient()
        url = '/api/horarios/SCA/'

        # act
        response = client.get(url, format='json')
        result = json.loads(response.content)

        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], self.horario_0_expected_json)
        self.assertEqual(result[1], self.horario_1_expected_json)

        for horario in result:
            self.assertIn('dia_inicio', horario)
            self.assertIn('hora_inicio', horario)
            self.assertIn('dia_final', horario)
            self.assertIn('hora_final', horario)

    def test_get_horarios_by_id_feria_invalid(self):
        """Test get_horarios_by_id_feria_invalid"""

        # arrange
        client = APIClient()
        url = '/api/horarios/asdsad/'

        # act
        response = client.get(url, format='json')
        result = json.loads(response.content)

        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(result), 0)

    def test_get_horarios_invalid_url(self):
        """Test get_horarios_invalid_url"""

        # arrange
        client = APIClient()
        url = '/api/horarios'

        # act
        response = client.get(url, format='json')

        # assert
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
