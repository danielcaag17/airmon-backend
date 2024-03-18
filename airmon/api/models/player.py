from django.db import models

from .location import Location
from .user import User


class Player (User):
    # PositiveSmallIntegerField amb rang [0-32767]
    # PositiveIntegerField amb rang [0-2147483647]
    # RT10 garantida
    xp_points = models.PositiveSmallIntegerField()
    coins = models.PositiveSmallIntegerField()
    # En cas que la ubicacio associada s'elimini, l'atribut actualLocation es posa a NULL
    actual_location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)

