from django.db import models

from .airmon import Airmon
from .user import User


class Capture (models.Model):
    # En cas que s'elimini l'Airmon o l'Usuari s'elimen totes les captures que es relacionen
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    # airmon conte name, rarity i type de l'airmon associat
    airmon = models.ForeignKey(Airmon, on_delete=models.CASCADE)
    date = models.DateTimeField()
    attempts = models.PositiveSmallIntegerField()

    # Clau primaria User+Data o User+Airmon
    class Meta:
        unique_together = ('airmon', 'username', 'date')
