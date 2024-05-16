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
    avatar = models.ImageField(default=None, null=True, upload_to='avatars/')

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
