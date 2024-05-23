from django.db.models.signals import post_save
from django.dispatch import receiver
from ..models import Capture, Player


@receiver(post_save, sender=Capture)
def capture_created(sender, instance, created, **kwargs):
    if created:
        player = Player.objects.get(username=instance.username)
        player.n_airmons_capturats += 1
    else:
        print(f'User {instance.username} has been updated.')
