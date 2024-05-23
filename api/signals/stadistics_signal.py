from django.db.models.signals import post_save
from django.dispatch import receiver
from ..models import Capture


@receiver(post_save, sender=Capture)
def capture_created(sender, instance, created, **kwargs):
    if created:
        print(f'User {instance.username} has been created.')
    else:
        print(f'User {instance.username} has been updated.')
