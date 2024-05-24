from api.models.rarity_type import RarityType
from api.models.airmon_type import AirmonType

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


def get_airmons():
    return airmons
