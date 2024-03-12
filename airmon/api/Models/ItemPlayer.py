from django.db import models

from airmon.api.Models.Item import Item
from airmon.api.Models.User import User


class ItemPlayer (models.Model):
    # En cas que s'elimini l'Item o l'Usuari s'elimen tots els ItemPlayer que es relacionen
    itemName = models.ForeignKey(Item, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = ('itemName', 'username')
