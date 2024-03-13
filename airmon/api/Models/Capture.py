from django.db import models

from airmon.api.Models.Aimon import Airmon
from airmon.api.Models.User import User


class Capture (models.Model):
    # En cas que s'elimini l'Airmon o l'Usuari s'elimen totes les captures que es relacionen
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    airmonName = models.ForeignKey(Airmon, on_delete=models.CASCADE, to_field='airmonName')
    rarity = models.ForeignKey(Airmon, on_delete=models.CASCADE, to_field='rarity')
    type = models.ForeignKey(Airmon, on_delete=models.CASCADE, to_field='type')
    date = models.DateTimeField()
    attemps = models.PositiveSmallIntegerField()

    # Clau primaria User+Data o User+Airmon
    class Meta:
        unique_together = (('username', 'airmonName', 'rarity', 'type'), ('username', 'date'))
