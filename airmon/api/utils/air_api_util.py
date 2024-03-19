import json
from datetime import datetime, timedelta
from django.apps import apps
from decimal import Decimal

from .requester import Requester
from ..models import Station, Pollutant, PollutantMeasure, Measure, Location, UnitType


url = "https://analisi.transparenciacatalunya.cat/resource/tasf-thgu.json"
client = Requester(url)


def update_air_data():
    """
    Updates the air data in the database
    """

    data = _request_air_data()
    print(json.dumps(data, indent=4))

    for info in data:

        longitude = Decimal(info["longitud"])
        latitude = Decimal(info["latitud"])

        if (loc := _check_model_exists("Location", longitude=longitude, latitude=latitude)) is None:
            loc = Location.objects.create(longitude=longitude, latitude=latitude)

        station, created = Station.objects.update_or_create(
            code=info["codi_eoi"],
            defaults={'name': info["nom_estacio"], 'location': loc}
        )

        pollutant, created = Pollutant.objects.update_or_create(
            name=info["contaminant"],
            defaults={'measure_unit': _parse_pollutant_measure(info["unitats"]), 'recommended_limit': 1.0}
        )

        time = datetime.strptime(info["data"], "%Y-%m-%dT%H:%M:%S.%f")

        measure, created = Measure.objects.update_or_create(
            station_code=station, date=time.date(), hour=time.time(),
            defaults={'station_code': station, 'date': time.date(), 'hour': time.time()}
        )

        PollutantMeasure.objects.update_or_create(
            pollutant_name=pollutant, measure=measure, quantity=info["h04"],
            defaults={'pollutant_name': pollutant, 'measure': measure, 'quantity': info["h04"]}
        )

    print("Air data updated")


def _parse_pollutant_measure(measure):
    if measure == "mg/m3":
        return UnitType.MILIGRAMSxMETRES3.value

    if measure == "µg/m3":
        return UnitType.MICROGRAMSxMETRE3.value


def _request_air_data():
    """
    Requests air data from the air quality API
    """

    date = datetime.now()
    data = date - timedelta(days=1)
    date = date.replace(hour=0, minute=0, second=0, microsecond=0)
    date = date.isoformat()

    return client.get(limit=1, where=f"data='{date}'")


def _check_model_exists(model_name, **kwargs):
    """
    Checks if a model exists in the database
    """
    model = apps.get_model('api', model_name)
    print(model, kwargs)
    res = model.objects.filter(**kwargs).first()
    print(res)
    return res
