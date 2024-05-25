from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from ..models import Player, PlayerTrophy, Trophy

player_field = {
    "Caçador Mestre": "n_airmons_capturats",
    "Llibertador d’Esperits": "airmons_alliberats",
    "Col·leccionista quotidià": "total_airmons_common",
    "Explorador Especial": "total_airmons_special",
    "Caçador Èpic": "total_airmons_epic",
    "Descobridor Mític": "total_airmons_mythical",
    "Llegenda Vivent": "total_airmons_legendary",
    "Apostador Aeri": "n_tirades_ruleta",
    "Alquimista de Combat": "n_consumibles_usats",
    "Comprador Compulsiu": "total_compres",
    "Rei del Tresor": "total_coins",
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
