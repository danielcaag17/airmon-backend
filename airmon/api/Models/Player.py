from django.db import models
from airmon.api.Models.User import Usuari


class Jugador (Usuari):   # Hereda Usuari
    puntsXP = models.IntegerField()
    monedes = models.IntegerField()
    ubicacioActualX = models.IntegerField()
    ubicacioActualY = models.IntegerField()
