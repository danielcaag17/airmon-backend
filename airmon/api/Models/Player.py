from django.db import models

from airmon.api.Models.Location import Location
from airmon.api.Models.User import User


class Player (User):
    # PositiveSmallIntegerField amb rang [0-32767]
    # PositiveIntegerField amb rang [0-2147483647]
    XpPoints = models.PositiveSmallIntegerField()
    coins = models.PositiveSmallIntegerField()
    # En cas que la ubicacio associada s'elimini, l'atribut actualLocation es posa a NULL
    actualLocation = models.ForeignKey(Location, on_delete=models.SET_NULL)

