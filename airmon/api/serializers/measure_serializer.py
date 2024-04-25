from datetime import time

from rest_framework import serializers
from .pollutant_measure_serializer import PollutantMeasureSerializer
from ..models import Measure, PollutantMeasure


class MeasureSerializer(serializers.ModelSerializer):
    pollutants = serializers.SerializerMethodField()
    val_color = serializers.SerializerMethodField()
    nom_pollutant = serializers.SerializerMethodField()
    hour = serializers.SerializerMethodField()

    class Meta:
        model = Measure
        fields = ['date', 'hour', 'val_color', 'nom_pollutant', 'pollutants']

    def get_hour(self, obj):
        if obj.hour is None:
            return time(hour=0, minute=0, second=0).strftime('%H:%M:%S')
        else:
            return obj.hour.strftime('%H:%M:%S')

    def get_pollutants(self, obj):
        pollutants = PollutantMeasure.objects.filter(measure_id=obj.id)
        serializer = PollutantMeasureSerializer(pollutants, many=True)
        return serializer.data

    def get_val_color(self, obj):
        pollutants = PollutantMeasure.objects.filter(measure_id=obj)
        val_color = self.calcularICQA(pollutants, "color")
        return val_color

    def get_nom_pollutant(self, obj):
        pollutants = PollutantMeasure.objects.filter(measure_id=obj)
        nom_pollutant = self.calcularICQA(pollutants, "nom")
        return nom_pollutant

    def calcularICQA(self, pollutants, type):
        val_max = 0
        val_color = 0
        nom_pollutant = ""
        for pollutant in pollutants:
            if pollutants.exists():
                name = pollutant.pollutant_name.name
                quantity = pollutant.quantity
                if name == "NO2":
                    if quantity <= 40:
                        val_color = 1
                    elif quantity <= 90:
                        val_color = 2
                    elif quantity <= 120:
                        val_color = 3
                    elif quantity <= 230:
                        val_color = 4
                    elif quantity <= 340:
                        val_color = 5
                    else:
                        val_color = 6
                elif name == "PM10":
                    if quantity <= 20:
                        val_color = 1
                    elif quantity <= 40:
                        val_color = 2
                    elif quantity <= 50:
                        val_color = 3
                    elif quantity <= 100:
                        val_color = 4
                    elif quantity <= 150:
                        val_color = 5
                    else:
                        val_color = 6
                elif name == "PM2.5":
                    if quantity <= 10:
                        val_color = 1
                    elif quantity <= 20:
                        val_color = 2
                    elif quantity <= 25:
                        val_color = 3
                    elif quantity <= 50:
                        val_color = 4
                    elif quantity <= 75:
                        val_color = 5
                    else:
                        val_color = 6
                elif name == "O3":
                    if quantity <= 50:
                        val_color = 1
                    elif quantity <= 100:
                        val_color = 2
                    elif quantity <= 130:
                        val_color = 3
                    elif quantity <= 240:
                        val_color = 4
                    elif quantity <= 380:
                        val_color = 5
                    else:
                        val_color = 6
                elif name == "SO2":
                    if quantity <= 100:
                        val_color = 1
                    elif quantity <= 200:
                        val_color = 2
                    elif quantity <= 350:
                        val_color = 3
                    elif quantity <= 500:
                        val_color = 4
                    elif quantity <= 750:
                        val_color = 5
                    else:
                        val_color = 6
                elif name == "CO":
                    if quantity <= 2:
                        val_color = 1
                    elif quantity <= 5:
                        val_color = 2
                    elif quantity <= 10:
                        val_color = 3
                    elif quantity <= 20:
                        val_color = 4
                    elif quantity <= 50:
                        val_color = 5
                    else:
                        val_color = 6
                elif name == "C6H6":
                    if quantity <= 5:
                        val_color = 1
                    elif quantity <= 10:
                        val_color = 2
                    elif quantity <= 20:
                        val_color = 3
                    elif quantity <= 50:
                        val_color = 4
                    elif quantity <= 100:
                        val_color = 5
                    else:
                        val_color = 6
                elif name == "H2S":
                    if quantity <= 25:
                        val_color = 1
                    elif quantity <= 50:
                        val_color = 2
                    elif quantity <= 100:
                        val_color = 3
                    elif quantity <= 200:
                        val_color = 4
                    elif quantity <= 500:
                        val_color = 5
                    else:
                        val_color = 6

                # Veure quins pollutants no es tenen en compte
                else:
                    print(name)

                if val_max < val_color:
                    val_max = val_color
                    nom_pollutant = name
        if type == "color":
            return val_max
        else:
            return nom_pollutant
