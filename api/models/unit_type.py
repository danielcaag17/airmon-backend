from django.db import models


class UnitType(models.TextChoices):
    MICROGRAMSxMETRE3 = "Micrograms/m3"
    MILIGRAMSxMETRES3 = "Miligrams/m3"
