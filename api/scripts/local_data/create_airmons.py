from api.scripts.django_setup import setup_django

setup_django()

from api.models.airmon import Airmon
from api.models.rarity_type import RarityType
from api.models.airmon_type import AirmonType

airmons = [
    {
        "name": "Bidoof",
        "description": "",
        "rarity": RarityType.COMU,
        "type": AirmonType.LOREM,
        "image": None,
    },
    {
        "name": "Rattata",
        "description": "",
        "rarity": RarityType.COMU,
        "type": AirmonType.LOREM,
        "image": None,
    },
    {
        "name": "Charmander",
        "description": "",
        "rarity": RarityType.ESPECIAL,
        "type": AirmonType.LOREM,
        "image": None,
    },
    {
        "name": "Bulbasur",
        "description": "",
        "rarity": RarityType.ESPECIAL,
        "type": AirmonType.LOREM,
        "image": None,
    },
    {
        "name": "Squirtle",
        "description": "",
        "rarity": RarityType.ESPECIAL,
        "type": AirmonType.LOREM,
        "image": None,
    },
    {
        "name": "Pikachu",
        "description": "",
        "rarity": RarityType.CURIOS,
        "type": AirmonType.LOREM,
        "image": None,
    },
    {
        "name": "Charmeleon",
        "description": "",
        "rarity": RarityType.CURIOS,
        "type": AirmonType.LOREM,
        "image": None,
    },
    {
        "name": "Ivysaur",
        "description": "",
        "rarity": RarityType.CURIOS,
        "type": AirmonType.LOREM,
        "image": None,
    },
    {
        "name": "Wartortle",
        "description": "",
        "rarity": RarityType.CURIOS,
        "type": AirmonType.LOREM,
        "image": None,
    },
    {
        "name": "Charizard",
        "description": "",
        "rarity": RarityType.EPIC,
        "type": AirmonType.LOREM,
        "image": None,
    },
    {
        "name": "Venusaur",
        "description": "",
        "rarity": RarityType.EPIC,
        "type": AirmonType.LOREM,
        "image": None,
    },
    {
        "name": "Blastoise",
        "description": "",
        "rarity": RarityType.EPIC,
        "type": AirmonType.LOREM,
        "image": None,
    },
    {
        "name": "Arceus",
        "description": "",
        "rarity": RarityType.LLEGENDARI,
        "type": AirmonType.LOREM,
        "image": None,
    },
]

new_airmons = []
for airmon in airmons:
    new_airmons.append(
        Airmon(
            name=airmon["name"],
            description=airmon["description"],
            rarity=airmon["rarity"].value,
            type=airmon["type"].value,
            image=airmon["image"],
        )
    )
Airmon.objects.bulk_create(
    new_airmons,
    update_conflicts=True,
    unique_fields=["name"],
    update_fields=["description", "rarity", "type", "image"],
)
