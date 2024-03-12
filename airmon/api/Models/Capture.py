from django.db import models

from airmon.api.Models.Aimon import Airmon
from airmon.api.Models.User import User


class Capture (models.Model):
    # En cas que s'elimini l'Airmon o l'Usuari s'elimen totes les captures que es relacionen
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    airmonName = models.ForeignKey(Airmon, on_delete=models.CASCADE)
    date = models.DateTimeField()
    attemps = models.PositiveSmallIntegerField()

    # Clau primaria User+Data o User+Airmon
    class PK:
        unique_together = (('username', 'airmonName'), ('username', 'date'))
