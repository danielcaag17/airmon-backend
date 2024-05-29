from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from ..models import Player, PlayerTrophy, Trophy

player_field = {
    "trophy1": "n_airmons_capturats",
    "trophy2": "airmons_alliberats",
    "trophy3": "total_airmons_common",
    "trophy4": "total_airmons_special",
    "trophy5": "total_airmons_epic",
    "trophy6": "total_airmons_mythical",
    "trophy7": "total_airmons_legendary",
    "trophy8": "n_tirades_ruleta",
    "trophy9": "n_consumibles_usats",
    "trophy10": "total_compres",
    "trophy11": "total_coins",
}


@receiver(post_save, sender=Player)
def player_updated(sender, instance, created, **kwargs):
    if created:
        pass
    else:
        # TODO: veure un manera més eficient
        trophies = Trophy.objects.all()
        for trophy in trophies:
            obtenir_trofeu(instance, player_field[trophy.name], trophy)


def obtenir_trofeu(instance, field, trophy):
    field_value = getattr(instance, field)
    if field_value >= trophy.requirement:
        player_trophy, created = PlayerTrophy.objects.get_or_create(user=instance.user,
                                                                    trophy=trophy,
                                                                    defaults={'date': timezone.now()})
        if created:
            instance.xp_points += trophy.xp
            instance.save(update_fields=['xp_points'])


def get_relation():
    return player_field
