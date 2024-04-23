from django.contrib.auth.models import User
from django.db import models

from . import Language
from .location import Location


class Player(models.Model):
    # PositiveSmallIntegerField amb rang [0-32767]
    # PositiveIntegerField amb rang [0-2147483647]
    # RT10 garantida
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    language = models.CharField(max_length=16, choices=[(tag, tag.value) for tag in Language],
                                default=Language.CATALA.value)
    xp_points = models.PositiveSmallIntegerField(default=0)
    coins = models.PositiveSmallIntegerField(default=0)
    avatar = models.ImageField(null=True, upload_to='avatars/')
    # PUBLISHED IMAGES


class PlayerImages(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, upload_to='uploaded/')


