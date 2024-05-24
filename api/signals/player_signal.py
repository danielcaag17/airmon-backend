from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User

from .utils import get_raresa
from ..models import Capture, Player, PlayerItem, PlayerActiveItem

# Utilitzat per guardar instàncies abans de fer el save
old_values_cache = {}


@receiver(post_save, sender=User)
def user_created(sender, instance, created, **kwargs):
    if created:
        user = User.objects.get(username=instance.username)
        Player.objects.create(user=user, avatar=None)
    else:
        pass


@receiver(pre_save, sender=Player)
def player_old_values(sender, instance, **kwargs):
    try:
        if instance.pk:
            old_instance = Player.objects.get(pk=instance.pk)
            old_values_cache[instance.pk] = {
                "coins": old_instance.coins,
                "roulette": old_instance.last_roulette_spin
            }
    except Player.DoesNotExist:
        old_values_cache[instance.pk] = {
            'coins': None,
            'last_roulette_spin': None,
        }


@receiver(post_save, sender=Player)
def player_updated(sender, instance, created, **kwargs):
    if created:
        pass
    else:
        old_instance = old_values_cache.get(instance.pk)
        old_coins = old_instance.get("coins")
        new_coins = instance.coins
        old_roulette = old_instance.get("roulette")
        new_roulette = instance.last_roulette_spin
        if old_coins != new_coins:
            # Player ha obtingut monedas
            if old_coins is not None and old_coins < new_coins:
                # Sumar la diferència de monedes que ha guanyat
                instance.total_coins += new_coins - old_coins
                instance.save(update_fields=['total_coins'])
        if old_roulette != new_roulette:
            instance.n_tirades_ruleta += 1
            instance.save(update_fields=['n_tirades_ruleta'])
        old_values_cache.pop(instance.pk, None)


@receiver(pre_save, sender=PlayerItem)
def player_item_old_values(sender, instance, **kwargs):
    if instance.pk:
        old_instance = PlayerItem.objects.get(pk=instance.pk)
        old_values_cache[instance.pk] = old_instance.quantity


@receiver(post_save, sender=PlayerItem)
def player_item_created(sender, instance, created, **kwargs):
    if created:
        player = Player.objects.get(user__username=instance.user)
        player.total_compres += instance.quantity
        player.save(update_fields=['total_compres'])
    else:
        old_quantity = old_values_cache.get(instance.pk)
        new_quantity = instance.quantity

        # Player ha comprat item
        if old_quantity is not None and old_quantity < new_quantity:
            player = Player.objects.get(user__username=instance.user)
            player.total_compres += new_quantity - old_quantity
            player.save(update_fields=['total_compres'])

        old_values_cache.pop(instance.pk, None)


@receiver(post_save, sender=PlayerActiveItem)
def player_active_item_created(sender, instance, created, **kwargs):
    if created:
        player = Player.objects.get(user=instance.user_id)
        player.n_consumibles_usats += 1
        player.save(update_fields=['n_consumibles_usats'])
    else:
        pass


@receiver(post_save, sender=Capture)
def capture_created(sender, instance, created, **kwargs):
    if created:
        player = Player.objects.get(user__username=instance.user)
        player.n_airmons_capturats += 1
        raresa = get_raresa(instance.airmon_id)
        if raresa in raresa_mapping:
            player_field = raresa_mapping[raresa]
            setattr(player, player_field, getattr(player, player_field) + 1)
        update_fields = ['n_airmons_capturats'] + [raresa_mapping[raresa]] if raresa in raresa_mapping else []
        player.save(update_fields=update_fields)
    else:
        pass


raresa_mapping = {
    "Legendary": "total_airmons_legendary",
    "Mythical": "total_airmons_mythical",
    "Epic": "total_airmons_epic",
    "Special": "total_airmons_special",
    "Common": "total_airmons_common"
}


@receiver(post_delete, sender=Capture)
def capture_post_delete(sender, instance, **kwargs):
    try:
        player = Player.objects.get(user__username=instance.user)
        player.airmons_alliberats += 1
        player.save(update_fields=['airmons_alliberats'])
    except Player.DoesNotExist:
        pass
