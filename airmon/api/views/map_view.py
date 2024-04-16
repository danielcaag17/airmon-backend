# from django.utils import timezone
from rest_framework.response import Response
from rest_framework import viewsets
from ..models import Measure, PollutantMeasure, Station

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
class MapViewSet(viewsets.ViewSet):
    """
    Endpoint: /api/map/
    """

    '''
    def afegir(self):
        nueva_instancia = Measure(
            station_code=Station.objects.get(code=1),
            date=timezone.now().date(),
            hour=timezone.now().time()
        )
        nueva_instancia.save()
    '''

    def calcularICQA(self, pollutants):
        val_max = 0
        val_color = 0
        nom_pollutant = ""
        for pollutant in pollutants:
            if pollutant["pollutant_name"] == "NO2":
                if pollutant["quantity"] <= 40:
                    val_color = 1
                elif pollutant["quantity"] <= 90:
                    val_color = 2
                if pollutant["quantity"] <= 120:
                    val_color = 3
                if pollutant["quantity"] <= 230:
                    val_color = 4
                if pollutant["quantity"] <= 340:
                    val_color = 5
                else:
                    val_color = 6
            elif pollutant["pollutant_name"] == "PM10":
                if pollutant["quantity"] <= 20:
                    val_color = 1
                elif pollutant["quantity"] <= 40:
                    val_color = 2
                if pollutant["quantity"] <= 50:
                    val_color = 3
                if pollutant["quantity"] <= 100:
                    val_color = 4
                if pollutant["quantity"] <= 150:
                    val_color = 5
                else:
                    val_color = 6
            elif pollutant["pollutant_name"] == "PM2":
                if pollutant["quantity"] <= 10:
                    val_color = 1
                elif pollutant["quantity"] <= 20:
                    val_color = 2
                if pollutant["quantity"] <= 25:
                    val_color = 3
                if pollutant["quantity"] <= 50:
                    val_color = 4
                if pollutant["quantity"] <= 75:
                    val_color = 5
                else:
                    val_color = 6
            elif pollutant["pollutant_name"] == "O3":
                if pollutant["quantity"] <= 50:
                    val_color = 1
                elif pollutant["quantity"] <= 100:
                    val_color = 2
                if pollutant["quantity"] <= 130:
                    val_color = 3
                if pollutant["quantity"] <= 240:
                    val_color = 4
                if pollutant["quantity"] <= 380:
                    val_color = 5
                else:
                    val_color = 6
            elif pollutant["pollutant_name"] == "SO2":
                if pollutant["quantity"] <= 100:
                    val_color = 1
                elif pollutant["quantity"] <= 200:
                    val_color = 2
                if pollutant["quantity"] <= 350:
                    val_color = 3
                if pollutant["quantity"] <= 500:
                    val_color = 4
                if pollutant["quantity"] <= 750:
                    val_color = 5
                else:
                    val_color = 6
            elif pollutant["pollutant_name"] == "CO":
                if pollutant["quantity"] <= 2:
                    val_color = 1
                elif pollutant["quantity"] <= 5:
                    val_color = 2
                if pollutant["quantity"] <= 10:
                    val_color = 3
                if pollutant["quantity"] <= 20:
                    val_color = 4
                if pollutant["quantity"] <= 50:
                    val_color = 5
                else:
                    val_color = 6
            elif pollutant["pollutant_name"] == "C6H6":
                if pollutant["quantity"] <= 5:
                    val_color = 1
                elif pollutant["quantity"] <= 10:
                    val_color = 2
                if pollutant["quantity"] <= 20:
                    val_color = 3
                if pollutant["quantity"] <= 50:
                    val_color = 4
                if pollutant["quantity"] <= 100:
                    val_color = 5
                else:
                    val_color = 6
            elif pollutant["pollutant_name"] == "H2S":
                if pollutant["quantity"] <= 25:
                    val_color = 1
                elif pollutant["quantity"] <= 50:
                    val_color = 2
                if pollutant["quantity"] <= 100:
                    val_color = 3
                if pollutant["quantity"] <= 200:
                    val_color = 4
                if pollutant["quantity"] <= 500:
                    val_color = 5
                else:
                    val_color = 6
            # Veure quins pollutants no es tenen en compte
            else:
                print(pollutant["pollutant_name"])

            if val_max < val_color:
                val_max = val_color
                nom_pollutant = pollutant["pollutant_name"]

        return val_max, nom_pollutant

    def get_pollutants(self, measure_id):
        pollutant_measure = PollutantMeasure.objects.filter(measure_id=measure_id)
        pollutant_measure_serializer = []
        for objPM in pollutant_measure:
            pollutant_measure_obj_serialized = {
                'pollutant_name': objPM.pollutant_name.name,
                'measure_unit': objPM.pollutant_name.measure_unit,
                'quantity': objPM.quantity,
                'recommended_limit': objPM.pollutant_name.recommended_limit,
            }
            pollutant_measure_combined_data = {
                'pollutant': pollutant_measure_obj_serialized
            }
            pollutant_measure_serializer.append(pollutant_measure_combined_data)
        return pollutant_measure_serializer

    def get_measures(self, code):
        measure = Measure.objects.filter(station_code=code)
        measure_obj_serialized = {}
        for objM in measure:
            pollutants = self.get_pollutants(objM.id)
            # val_color entre 1 i 6, 1 Bona i 6 Extremadament desfavorable
            val_color, nom_pollutant = self.calcularICQA(pollutants)
            measure_obj_serialized = {
                'date': objM.date.strftime('%Y-%m-%d'),
                'hour': objM.date.strftime('%H:%M:%S'),
                'val_color': val_color,
                'nom_pollutant': nom_pollutant,
                'pollutants': pollutants,
            }
        return measure_obj_serialized

    def list(self, request):
        # self.afegir()
        station_serializer = []
        station = Station.objects.all()
        for objS in station:
            station_obj_serialized = {
                'code_station': objS.code,
                'name': objS.name,
                'longitude': objS.location.longitude,
                'latitude': objS.location.latitude,
                'measure': self.get_measures(objS.code),
            }
            station_serializer.append(station_obj_serialized)
        return Response(station_serializer)

