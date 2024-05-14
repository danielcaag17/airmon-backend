from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User


class Friendship(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user1_friendship')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user2_friendship')
    date = models.DateTimeField()

    def create(self, **kwargs):
        new_friendship = Friendship(**kwargs)
        new_friendship.clean()
        new_friendship.save()
        return new_friendship

    def clean(self):
        if self.user1 == self.user2:
            raise ValidationError('Users cannot be the same')

    class Meta:
        unique_together = [['user1', 'user2'], ['user2', 'user1']]
