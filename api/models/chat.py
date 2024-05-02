from django.db import models
from django.contrib.auth.models import User
from django.db.models import F, Q


class Chat(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chats1')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chats2')

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=~Q(user1=F('user2')),
                name='different_users_chat'
            ),
        ]
        unique_together = ('user1', 'user2')


class ChatMessage(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    message = models.TextField(max_length=10000)
    date = models.DateTimeField(auto_now_add=True)
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    read = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=~Q(from_user=F('to_user')),
                name='different_users_message'
            ),
        ]
        unique_together = ('from_user', 'to_user', 'date')
        ordering = ['date']
