# from django.utils import timezone
from rest_framework.response import Response
from rest_framework import viewsets
from ..models import Measure
from ..models import PollutantMeasure
from ..models import Pollutant
from ..models import Station


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

    def list(self, request):
        # self.afegir()

        '''
        measure = Measure.objects.all()
        pollutant_measure = PollutantMeasure.objects.all()
        pollutant = Pollutant.objects.all()
        station = Station.objects.all()

        measure_serializer = []
        # i = measure.first().station_code.code
        for obj in measure:
            obj_serialized = {
                'station_code': obj.station_code.code,
                'date': obj.date.strftime('%Y-%m-%d'),
                'hour': obj.date.strftime('%H:%M:%S'),
            }
            measure_serializer.append(obj_serialized)

        pollutant_measure_serializer = []
        for obj in pollutant_measure:
            obj_serialized = {
                'pollutant_name': obj.pollutant_name.name,
                # 'measure': obj.measure.station_code.code,
                'measure': obj.measure.id,
                'quantity': obj.quantity,
            }
            pollutant_measure_serializer.append(obj_serialized)

        pollutant_serializer = []
        for obj in pollutant:
            obj_serialized = {
                'name': obj.name,
                'measure_unit': obj.measure_unit,
                'recommended_limit': obj.recommended_limit,
            }
            pollutant_serializer.append(obj_serialized)
        '''
        final_result = []
        station_serializer = []
        station = Station.objects.all()
        station_combined_data = {}
        for objS in station:

            measure = Measure.objects.filter(station_code=objS.code)
            measure_combined_data = {}
            measure_serializer = []
            for objM in measure:

                pollutant_measure = PollutantMeasure.objects.filter(measure_id=objM.id)
                pollutant_measure_combined_data = {}
                pollutant_measure_serializer = []
                for objPM in pollutant_measure:
                    obj_pm_serialized = {
                        'pollutant_name': objPM.pollutant_name.name,
                        'measure_unit': objPM.pollutant_name.measure_unit,
                        'quantity': objPM.quantity,
                        'recommended_limit': objPM.pollutant_name.recommended_limit,
                    }
                    pollutant_measure_combined_data = {
                        'pollutant': obj_pm_serialized
                    }
                    pollutant_measure_serializer.append(pollutant_measure_combined_data)

                obj_m_serialized = {
                    'date': objM.date.strftime('%Y-%m-%d'),
                    'hour': objM.date.strftime('%H:%M:%S'),
                    'allPollutants': pollutant_measure_serializer,
                }
                measure_combined_data = {
                    'measure': obj_m_serialized
                }
                measure_serializer.append(measure_combined_data)

            obj_s_serialized = {
                'code_station': objS.code,
                'name': objS.name,
                'longitude': objS.location.longitude,
                'latitude': objS.location.latitude,
                'measures': measure_serializer,
            }
            station_serializer.append(obj_s_serialized)
            # station_serializer.append(measure_serializer)
            station_combined_data = {
                'station': station_serializer,
                # 'measure': measure_serializer,
                # 'pollutant': pollutant_serializer,
            }
        final_result.append(station_combined_data)
        return Response(final_result)

