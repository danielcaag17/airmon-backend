from django.db import models


class AirmonType(models.TextChoices):
    NO2 = "NO2"
    PM10 = "PM10"
    PM25 = "PM25"
    O3 = "O3"
    SO2 = "SO2"
    CO = "CO"
    C6H6 = "C6H6"
    H2S = "H2S"
