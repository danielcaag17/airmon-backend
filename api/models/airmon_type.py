from django.db import models


class AirmonType(models.TextChoices):
    LOREM = "Lorem"
    IPSUM = "Ipsum"
    DOLOR = "Dolor"
