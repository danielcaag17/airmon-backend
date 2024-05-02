from django.db import models


class RarityType(models.TextChoices):
    LLEGENDARI = 'Llegendari'
    EPIC = "Epic"
    CURIOS = 'Curios'
    ESPECIAL = 'Especial'
    COMU = 'Comu'
