from django.db import models


class RarityType(models.TextChoices):
    LEGENDARY = "LEGENDARY"
    MYTHICAL = "MYTHICAL"
    EPIC = "EPIC"
    SPECIAL = "SPECIAL"
    COMMON = "COMMON"
