from django.core.exceptions import ValidationError
from django.db import models
import pytz
from datetime import datetime
from django.contrib.auth.models import User


class Friendship(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user1_friendship')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user2_friendship')
    date = models.DateTimeField()

    def save(self, *args, **kwargs):
        timezone = pytz.timezone("Europe/Madrid")
        if self.date > datetime.now(timezone):
            raise ValueError("The date cannot be in the future.")
        if self.user1 == self.user2:
            raise ValidationError('Users cannot be the same.')
        if Friendship.objects.filter(user1=self.user2, user2=self.user1).exists():
            raise ValidationError('The friendship already exists.')
        else:
            super().save(*args, **kwargs)

    class Meta:
        unique_together = ['user1', 'user2']
