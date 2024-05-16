from datetime import datetime
import requests
from datetime import date
from decimal import Decimal, ROUND_DOWN
from django.apps import apps

from ..models import Event, LocationGeohash


url = "https://culturify.azurewebsites.net/events/aire_lliure/"
token = "Token 064050afcc548f7447f29e203189aee2db9d2063"
headers = {
    "Authorization": token
}


def update_event_data():
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        # Obtenir los dades de la resposta en format JSON
        data = response.json()

        for element in data:
            data_inici = datetime.strptime(element["data_inici"], "%Y-%m-%dT%H:%M:%S.%f").date()
            data_fi = datetime.strptime(element["data_fi"], "%Y-%m-%dT%H:%M:%S.%f").date()
            # Events que estan actius a dia d'avui
            if is_valid(data_inici, data_fi):
                if not event_exists(element["codi"]):
                    geohash = get_geohash(element)
                    Event.objects.create(
                        codi=element["codi"],
                        denominacio=element["denominaci"],
                        data_ini=data_inici,
                        data_fi=data_fi,
                        geohash=geohash,
                        espai=element["espai"]
                    )
            else:
                if event_exists(element["codi"]):
                    Event.objects.filter(codi=element["codi"]).delte()
    else:
        print("error al fer la crida al servei extern:", response.status_code)


def is_valid(data_inici, data_fi):
    avui = date.today()
    if data_inici <= avui <= data_fi:
        return True
    return False


def event_exists(codi):
    return Event.objects.filter(codi=codi).exists()


def get_geohash(element):
    longitude = round_decimal(Decimal(element["longitud"]), 6)
    latitude = round_decimal(Decimal(element["latitud"]), 6)

    # Transformar coordenades a geohash
    geohash = LocationGeohash.objects.coords_to_geohash(latitude=latitude, longitude=longitude)

    if (loc := _check_model_exists("LocationGeohash", geohash=geohash)) is None:
        loc = LocationGeohash.objects.create(geohash=geohash)
    return loc


def round_decimal(value, decimal_places):
    return value.quantize(Decimal(10) ** -decimal_places, rounding=ROUND_DOWN)


def _check_model_exists(model_name, **kwargs):
    """
    Checks if a model exists in the database
    """
    model = apps.get_model('api', model_name)
    res = model.objects.filter(**kwargs).first()
    return res
