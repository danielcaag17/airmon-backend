from django.db import models

from .item import Item
from .user import User


class PlayerItem (models.Model):
    # En cas que s'elimini l'Item o l'Usuari s'elimen tots els ItemPlayer que es relacionen
    item_name = models.ForeignKey(Item, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = ('item_name', 'username')
