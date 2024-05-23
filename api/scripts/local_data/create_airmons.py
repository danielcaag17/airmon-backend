def create_airmons():
    import os
    from django.core.files import File
    from django.conf import settings

    from api.models.airmon import Airmon
    from api.models.rarity_type import RarityType
    from api.models.airmon_type import AirmonType

    # Define the path to the temp folder
    temp_folder = os.path.join(settings.BASE_DIR, "temp_airmon_pictures")
    pokemons = [
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
    airmons = [
        {
            "name": "Smogreon",
            "description": "A nocturnal airmon shrouded in smog, it detoxifies polluted air. Its mysterious aura warns of environmental hazards.",
            "rarity": RarityType.COMMON,
            "type": AirmonType.NO2,
        },
        {
            "name": "Nitroxidus",
            "description": "A sleek Pokémon emitting a blue haze, it purifies air with its tail. Adaptable to urban environments, it thrives on NO2-rich air.",
            "rarity": RarityType.LEGENDARY,
            "type": AirmonType.NO2,
        },
        {
            "name": "Nitraxel",
            "description": "A nimble creature with vibrant yellow markings, it disperses toxic gases using its wings. Its presence signals clean air nearby.",
            "rarity": RarityType.EPIC,
            "type": AirmonType.NO2,
        },
        {
            "name": "Traffixir",
            "description": "This sturdy Pokémon has a metallic sheen and absorbs NO2 emissions. It evolves near heavy traffic areas, combating pollution.",
            "rarity": RarityType.MYTHICAL,
            "type": AirmonType.NO2,
        },
        {
            "name": "Industriox",
            "description": "With smokestack-like horns, it thrives in industrial zones, neutralizing NO2. Its robust frame withstands harsh pollutants.",
            "rarity": RarityType.SPECIAL,
            "type": AirmonType.NO2,
        },
        {
            "name": "Ozonox",
            "description": "A swift airmon that purifies its surroundings. Its shimmering body releases bursts of ozone to combat pollutants.",
            "rarity": RarityType.COMMON,
            "type": AirmonType.O3,
        },
        {
            "name": "Aethertox",
            "description": "Emitting a faint, bluish glow, Aethertox neutralizes harmful gases with its ethereal touch, purifying the air effortlessly.",
            "rarity": RarityType.MYTHICAL,
            "type": AirmonType.O3,
        },
        {
            "name": "Nitrofume",
            "description": "Cloaked in a hazy veil, Nitrofume absorbs nitrogen compounds, transforming toxic fumes into breathable air with its mystical aura.",
            "rarity": RarityType.EPIC,
            "type": AirmonType.O3,
        },
        {
            "name": "Chimireek",
            "description": "This enigmatic airmon thrives in polluted environments, exhaling ozone-rich clouds that cleanse the atmosphere of industrial toxins.",
            "rarity": RarityType.SPECIAL,
            "type": AirmonType.O3,
        },
        {
            "name": "Exhauxane",
            "description": "An airmon born from urban smog, Exhauxane converts vehicle emissions into fresh air, its metallic sheen reflecting its pollution-fighting prowess.",
            "rarity": RarityType.MYTHICAL,
            "type": AirmonType.O3,
        },
        # {
        #     "name": "Benzoair",
        #     "description": "This sturdy Pokémon has a metallic sheen and absorbs O3 emissions. It evolves near heavy traffic areas, combating pollution.",
        #     "rarity": RarityType.MYTHICAL,
        #     "type": AirmonType.C6H6,
        # },
    ]
    Airmon.objects.all().delete()
    new_airmons = []
    for airmon in airmons:
        image_path = os.path.join(temp_folder, f"{airmon['name']}.png")
        new_airmon = Airmon(
            name=airmon["name"],
            description=airmon["description"],
            rarity=airmon["rarity"].value,
            type=airmon["type"].value,
        )

        with open(image_path, "rb") as image_file:
            new_airmon.image.save(
                f"{airmon['name']}.png", File(image_file), save=False
            )
        new_airmons.append(new_airmon)
    Airmon.objects.bulk_create(
        new_airmons,
        update_conflicts=True,
        unique_fields=["name"],
        update_fields=["description", "rarity", "type", "image"],
    )


if __name__ == "__main__":
    from api.scripts.django_setup import setup_django

    setup_django()
    create_airmons()
