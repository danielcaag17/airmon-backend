from ..models import Airmon


def get_raresa(airmon_name):
    airmon = Airmon.objects.get(name=airmon_name)
    return airmon.rarity


def handle_legenday(player):
    player.total_airmons_llegendari += 1


def handle_mythical(player):
    player.total_airmons_mythical += 1


def handle_epic(player):
    player.total_airmons_epic += 1


def handle_special(player):
    player.total_airmons_special += 1


def handle_common(player):
    player.total_airmons_comu += 1


def handle_default(player):
    print("Handling default case")
    pass


raresa_actions = {
    "Legendary": lambda player: handle_legenday(player),
    "Mythical": lambda player: handle_mythical(player),
    "Epic": lambda player: handle_epic(player),
    "Special": lambda player: handle_special(player),
    "Common": lambda player: handle_common(player),
}