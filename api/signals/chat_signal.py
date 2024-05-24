from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from ..models import Chat, Friendship


# Crear Chat quan es crea Friendship
@receiver(post_save, sender=Friendship)
def friendship_created(sender, instance, created, **kwargs):
    if created:
        Chat.objects.create(
            user1=instance.user1,
            user2=instance.user2
        )
    else:
        pass


# Eliminar Chat quan s'elimina Friendship
@receiver(pre_delete, sender=Friendship)
def capture_post_delete(sender, instance, **kwargs):
    try:
        Chat.objects.filter(user1=instance.user1, user2=instance.user2).first().delete()
    except Chat.DoesNotExist:
        # En algun moment previ s'ha eliminat
        pass
