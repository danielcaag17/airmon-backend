from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User

from ..models import Airmon, Capture, Player, PlayerItem, PlayerActiveItem

# Utilitzat per guardar instàncies abans de fer el save
old_values_cache = {}


# Crear Player quan es crea User
@receiver(post_save, sender=User)
def user_created(sender, instance, created, **kwargs):
    if created:
        user = User.objects.get(username=instance.username)
        Player.objects.create(user=user, avatar=None)
    else:
        pass


# Guardar atributs de Player abans de guardar-lo
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


# Actualitzar estadístiques del Player
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

        # Segona condició verifica que el Player ha obtingut monedes
        if old_coins is not None and old_coins < new_coins:
            # Sumar la diferència de monedes que ha guanyat
            instance.total_coins += new_coins - old_coins
            instance.save(update_fields=['total_coins'])

        if old_roulette is not None and old_roulette != new_roulette:
            instance.n_tirades_ruleta += 1
            instance.save(update_fields=['n_tirades_ruleta'])

        old_values_cache.pop(instance.pk, None)


# Guardar la quantitat de PlayerItem abans de guardar-lo
@receiver(pre_save, sender=PlayerItem)
def player_item_old_values(sender, instance, **kwargs):
    if instance.pk:
        old_instance = PlayerItem.objects.get(pk=instance.pk)
        old_values_cache[instance.pk] = old_instance.quantity


# Actualitzar atribut de Player
@receiver(post_save, sender=PlayerItem)
def player_item_created(sender, instance, created, **kwargs):
    if created:
        player = Player.objects.get(user__username=instance.user)
        player.total_compres += instance.quantity
        player.save(update_fields=['total_compres'])
    else:
        old_quantity = old_values_cache.get(instance.pk)
        new_quantity = instance.quantity

        # Segona condició verifica que Player ha comprat item
        if old_quantity is not None and old_quantity < new_quantity:
            player = Player.objects.get(user__username=instance.user)
            player.total_compres += new_quantity - old_quantity
            player.save(update_fields=['total_compres'])

        old_values_cache.pop(instance.pk, None)


# Actualitzar atribut de Player
@receiver(post_save, sender=PlayerActiveItem)
def player_active_item_created(sender, instance, created, **kwargs):
    if created:
        player = Player.objects.get(user=instance.user_id)
        player.n_consumibles_usats += 1
        player.save(update_fields=['n_consumibles_usats'])
    else:
        pass


# Actualitzar atributs de Player
@receiver(post_save, sender=Capture)
def capture_created(sender, instance, created, **kwargs):
    if created:
        player = Player.objects.get(user__username=instance.user)
        player.n_airmons_capturats += 1

        # Actualitzar atribut segons la raresa de l'Airmon
        airmon = Airmon.objects.get(name=instance.airmon_id)
        raresa = airmon.rarity
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


# Actualitzar quan s'allibera un Airmon
@receiver(post_delete, sender=Capture)
def capture_post_delete(sender, instance, **kwargs):
    try:
        player = Player.objects.get(user__username=instance.user)
        player.airmons_alliberats += 1
        player.save(update_fields=['airmons_alliberats'])
    except Player.DoesNotExist:
        pass
