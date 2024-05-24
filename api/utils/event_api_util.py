import requests
from django.utils import timezone

from .utils import get_geohash
from ..models import Event


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
        new_events = []

        for element in data:
            data_inici = timezone.datetime.strptime(element["data_inici"], "%Y-%m-%dT%H:%M:%S.%f").date()
            data_fi = timezone.datetime.strptime(element["data_fi"], "%Y-%m-%dT%H:%M:%S.%f").date()
            exists = event_exists(element["codi"])
            valid = is_valid(data_inici, data_fi)
            # Esdeveniments que estan actius el dia d'avui
            if valid and not exists:
                geohash = get_geohash(element)
                new_events.append(
                    Event(
                        codi=element["codi"],
                        denominacio=element["denominaci"],
                        data_ini=data_inici,
                        data_fi=data_fi,
                        geohash=geohash,
                        espai=element["espai"]
                    )
                )
            elif not valid and exists:
                Event.objects.filter(codi=element["codi"]).delete()

        Event.objects.bulk_create(
            new_events,
            update_conflicts=True,
            unique_fields=["codi"],
            update_fields=["denominacio", "data_ini", "data_fi", "geohash", "espai"],
        )

    else:
        raise Exception(f"error al fer la crida al servie extern {response.status_code}")


def is_valid(data_inici, data_fi):
    avui = timezone.now().date()
    if data_inici <= avui <= data_fi:
        return True
    return False


def event_exists(codi):
    return Event.objects.filter(codi=codi).exists()
