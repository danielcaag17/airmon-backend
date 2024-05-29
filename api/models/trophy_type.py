from django.db import models


class TrophyType(models.TextChoices):
    OR = "OR"
    PLATA = "PLATA"
    BRONZE = "BRONZE"
