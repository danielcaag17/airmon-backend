from django.db import models


class RarityType(models.TextChoices):
    LEGENDARY = 'Legendary'
    EPIC = "Epic"
    CURIOUS = 'Curious'
    SPECIAL = 'Special'
    COMMON = 'Common'
