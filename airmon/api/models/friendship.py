from django.db import models
from rest_framework.authtoken.admin import User


class FriendShip(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user1')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user2')
    date = models.DateTimeField()

    class Meta:
        # Falta comprovar quan es crea un usuari que no es ell mateix
        unique_together = [['user1', 'user2'], ['user2', 'user1']]
