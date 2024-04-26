from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse

from ..models import LocationGeohash, Station


class StationTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        LocationGeohash.objects.create(
            geohash='1'
        )
        Station.objects.create(
            code='1',
            name="Test Station",
            location_id=1
        )

    def test_station_creation(self):
        station = Station.objects.get(code='1')
        self.assertEqual(station.code, '1')

    '''
    def test_get_station(self):
        # Realizar una solicitud GET al endpoint
        response = self.client.get(reverse("get-station"), kwargs={"code": "1"})

        # Verificar que la solicitud sea exitosa (código de estado 200)
        self.assertEqual(response.status_code, 200)

        # Verificar que la respuesta sea JSON
        self.assertEqual(response["content-type"], "application/json")

        # Verificar que la respuesta contenga la lista de usuarios
        self.assertEqual(len(response.json()), 1)

        # Verificar el contenido de la respuesta
        self.assertEqual(response.json()[0]["id"], 1)
        self.assertEqual(response.json()[0]["name"], "Test Station")
    '''
