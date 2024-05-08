from django.db import models


class TrophyType(models.TextChoices):
    OR = "Or"
    PLATA = "Plata"
    BRONZE = "Bronze"
