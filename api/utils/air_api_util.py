from datetime import datetime, timedelta

from .requester import Requester
from .utils import get_geohash
from ..models import Station, Pollutant, PollutantMeasure, Measure, UnitType

url = "https://analisi.transparenciacatalunya.cat/resource/tasf-thgu.json"
client = Requester(url)


def update_air_data():
    """
    Updates the air data in the database
    """

    print("Updating air data")

    data = _request_air_data()

    PollutantMeasure.objects.all().delete()
    Measure.objects.all().delete()

    for info in data:

        measure_amount = _get_air_measurement(info)

        if measure_amount == -1:
            continue

        loc = get_geohash(info)

        station, created = Station.objects.update_or_create(
            code=info["codi_eoi"],
            defaults={'name': info["nom_estacio"], 'location': loc}
        )

        unit = _parse_pollutant_measure(info["unitats"])

        if unit is None:
            continue

        pollutant, created = Pollutant.objects.update_or_create(
            name=info["contaminant"],
            defaults={'measure_unit': unit}
        )

        time = datetime.strptime(info["data"], "%Y-%m-%dT%H:%M:%S.%f")

        measure, created = Measure.objects.get_or_create(
            station_code=station, date=time.date(), hour=time.time(),
            defaults={'station_code': station, 'date': time.date(), 'hour': time.time(), 'icqa': 0,
                      'nom_pollutant': "No pollutant"}
        )

        pollutant_measure, created = PollutantMeasure.objects.update_or_create(
            pollutant_name=pollutant, measure=measure,
            defaults={'pollutant_name': pollutant, 'measure': measure, 'quantity': measure_amount}
        )

        val, nom = calcular_icqa(pollutant_measure)
        if val > measure.icqa:
            measure.icqa = val
            measure.nom_pollutant = nom
            measure.save()


def _parse_pollutant_measure(measure):
    if measure == "mg/m3":
        return UnitType.MILIGRAMSxMETRES3.value
    elif measure == "µg/m3":
        return UnitType.MICROGRAMSxMETRE3.value
    else:
        return None


def _request_air_data():
    """
    Requests air data from the air quality API
    """

    date = datetime.now()
    date = date - timedelta(days=1)
    date = date.replace(hour=0, minute=0, second=0, microsecond=0)
    date = date.isoformat()

    return client.get(limit=500, where=f"data='{date}'")


def _get_air_measurement(data):
    """
    Checks if the data has the keys for the air quality measurements
    """
    measure = -1.0
    for key in data.keys():
        if key.startswith('h'):
            if float(data[key]) > measure:
                measure = float(data[key])

    return measure


def calcular_icqa(pollutant):  # noqa C901
    val_max = 1
    val_color = 1
    nom_pollutant = ""
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

    if val_max < val_color:
        val_max = val_color
        nom_pollutant = name
    return val_max, nom_pollutant
