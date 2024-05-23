from django.contrib.auth.models import User
from django.db import models

from . import Language


class Player(models.Model):
    # PositiveSmallIntegerField amb rang [0-32767]
    # PositiveIntegerField amb rang [0-2147483647]
    # RT10 garantida
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    language = models.CharField(max_length=16, choices=Language.choices, default=Language.CATALA)
    xp_points = models.PositiveSmallIntegerField(default=0)
    coins = models.PositiveSmallIntegerField(default=0)
    avatar = models.ImageField(null=True, upload_to='avatars/')

    # Estadístiques que s'han d'actualitzar cada cop
    n_airmons_capturats = models.PositiveSmallIntegerField(default=0)
    airmons_alliberats = models.PositiveSmallIntegerField(default=0)
    n_consumibles_usats = models.PositiveSmallIntegerField(default=0)
    n_tirades_ruleta = models.PositiveSmallIntegerField(default=0)
    total_coins = models.PositiveSmallIntegerField(default=0)
    total_airmons_common = models.PositiveSmallIntegerField(default=0)
    total_airmons_special = models.PositiveSmallIntegerField(default=0)
    total_airmons_epic = models.PositiveSmallIntegerField(default=0)
    total_airmons_mythical = models.PositiveSmallIntegerField(default=0)
    total_airmons_legendary = models.PositiveSmallIntegerField(default=0)
    total_compres = models.PositiveSmallIntegerField(default=0)

    # Estadistiques que es poden calcular
    # ...

    def save(self, *args, **kwargs):
        if self.language not in [choice[0] for choice in Language.choices]:
            raise ValueError("Invalid language value.")
        else:
            super().save(*args, **kwargs)


class PlayerImages(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, upload_to='uploaded/')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'date']
