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
            "description": "A sleek Airmon emitting a blue haze, it purifies air with its tail. Adaptable to urban environments, it thrives on NO2-rich air.",
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
            "description": "This sturdy Airmon has a metallic sheen and absorbs NO2 emissions. It evolves near heavy traffic areas, combating pollution.",
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
        {
            "name": "Particulon",
            "description": "A nimble and stealthy airmon, Particulon thrives in dense urban areas, using its particulate form to evade detection and strike swiftly.",
            "rarity": RarityType.LEGENDARY,
            "type": AirmonType.PM10,
        },
        {
            "name": "Sootalon",
            "description": "Dark and mysterious, Sootalon glides through industrial zones, its sooty wings leaving a trail of fine dust that can obscure its presence.",
            "rarity": RarityType.MYTHICAL,
            "type": AirmonType.PM10,
        },
        {
            "name": "Dustrix",
            "description": "Agile and elusive, Dustrix dances through the air, manipulating dust clouds to create intricate patterns that confuse and disorient its foes.",
            "rarity": RarityType.MYTHICAL,
            "type": AirmonType.PM10,
        },
        {
            "name": "Ashdrift",
            "description": "Emerging from the remnants of wildfires, Ashdrift is a resilient airmon that uses its ashen particles to form defensive barriers and attack with scorching precision.",
            "rarity": RarityType.MYTHICAL,
            "type": AirmonType.PM10,
        },
        {
            "name": "Fumory",
            "description": "Cloaked in a haze of fine smoke, Fumory moves silently through polluted skies, using its smoky tendrils to entangle and overwhelm opponents with smoggy bursts.",
            "rarity": RarityType.MYTHICAL,
            "type": AirmonType.PM10,
        },
        {
            "name": "Pollencloud",
            "description": "A whimsical airmon, Pollencloud drifts gently, dispersing allergenic particles. Its presence signals the start of spring and potential sneezes.",
            "rarity": RarityType.MYTHICAL,
            "type": AirmonType.PM25,
        },
        {
            "name": "Clogmist",
            "description": "Clogmist is dense and heavy, often found in industrial zones. Its thick fog impairs visibility and clogs the airways, making breathing difficult.",
            "rarity": RarityType.MYTHICAL,
            "type": AirmonType.PM25,
        },
        {
            "name": "Hazebur",
            "description": "Enveloped in a perpetual haze, Hazebur is elusive and tricky to spot. It often lingers in places with poor ventilation, causing persistent coughs.",
            "rarity": RarityType.MYTHICAL,
            "type": AirmonType.PM25,
        },
        {
            "name": "Dustveil",
            "description": "Shrouded in mystery, Dustveil cloaks itself in a fine layer of dust. It can blend into arid environments, stirring up particles with every movement.",
            "rarity": RarityType.MYTHICAL,
            "type": AirmonType.PM25,
        },
        {
            "name": "Noxiflare",
            "description": "Emitting a fiery glow, Noxiflare thrives in urban areas, feeding on pollutants. Its intense aura can cause irritation and discomfort to those nearby.",
            "rarity": RarityType.MYTHICAL,
            "type": AirmonType.PM25,
        },
        {
            "name": "Sulfuraise",
            "description": "Sulfuraise rises with industrial smoke, spreading its sulfuric aura and causing environmental distress.",
            "rarity": RarityType.MYTHICAL,
            "type": AirmonType.SO2,
        },
        {
            "name": "Chimnox",
            "description": "Often found near factories, Chimnox expels dark, harmful smoke that can linger in the air for days.",
            "rarity": RarityType.MYTHICAL,
            "type": AirmonType.SO2,
        },
        {
            "name": "Corrodeon",
            "description": "Corrodeon's corrosive emissions can damage metal structures, causing rust and decay over time.",
            "rarity": RarityType.MYTHICAL,
            "type": AirmonType.SO2,
        },
        {
            "name": "Sulfurnace",
            "description": "Sulfurnace's intense heat and sulfur emissions make it a walking furnace of pollution and smog.",
            "rarity": RarityType.MYTHICAL,
            "type": AirmonType.SO2,
        },
        {
            "name": "Clowst",
            "description": "Clowst normally tricks people to think it's a friendly airmon, but it brings sulfuric clouds wherever it goes.",
            "rarity": RarityType.MYTHICAL,
            "type": AirmonType.SO2,
        },
        {
            "name": "Exhaurox",
            "description": "This Airmon releases harmful gases from its vents, thriving in urban areas with heavy traffic and pollution.",
            "rarity": RarityType.MYTHICAL,
            "type": AirmonType.CO,
        },
        {
            "name": "Combusta",
            "description": "Known for its fiery emissions, Combusta is often found near factories and industrial zones, feeding off exhaust fumes.",
            "rarity": RarityType.MYTHICAL,
            "type": AirmonType.CO,
        },
        {
            "name": "Gascape",
            "description": "Gascape has a knack for slipping through cracks and vents, spreading invisible toxins wherever it goes.",
            "rarity": RarityType.MYTHICAL,
            "type": AirmonType.CO,
        },
        {
            "name": "Carbost",
            "description": "A master of disguise, Carbost mimics smoke and can drift through the air, leaving behind traces of soot and ash.",
            "rarity": RarityType.MYTHICAL,
            "type": AirmonType.CO,
        },
        {
            "name": "Fumigry",
            "description": "Fumigry loves hanging around construction sites, using its wings to stir up dust and release toxic fumes into the air.",
            "rarity": RarityType.MYTHICAL,
            "type": AirmonType.CO,
        },
        {
            "name": "Toxovent",
            "description": "Emitting hazardous gases, Toxovent lurks in underground tunnels, thriving on the noxious air found within.",
            "rarity": RarityType.MYTHICAL,
            "type": AirmonType.C6H6,
        },
        {
            "name": "Benzorin",
            "description": "Stealthy and swift, Benzorin navigates polluted skies, neutralizing benzene emissions with its electrifying aura.",
            "rarity": RarityType.MYTHICAL,
            "type": AirmonType.C6H6,
        },
        {
            "name": "Vaportox",
            "description": "Vaportox absorbs benzene vapors, converting them into harmless mist while floating gracefully through polluted air.",
            "rarity": RarityType.MYTHICAL,
            "type": AirmonType.C6H6,
        },
        {
            "name": "Benzorak",
            "description": "With a fiery spirit, Benzorak combats benzene pollutants, leaving behind a trail of purified air in its wake.",
            "rarity": RarityType.MYTHICAL,
            "type": AirmonType.C6H6,
        },
        {
            "name": "Smogloom",
            "description": "Mysterious and enigmatic, Smogloom thrives in polluted environments, absorbing benzene to nurture its dark aura.",
            "rarity": RarityType.MYTHICAL,
            "type": AirmonType.C6H6,
        },
        {
            "name": "Toxithorn",
            "description": "A spiky plant Airmon with thorns dripping with toxic chemicals, leaving a trail of contamination.",
            "rarity": RarityType.MYTHICAL,
            "type": AirmonType.H2S,
        },
        {
            "name": "Nitrognarl",
            "description": "A gnarled tree-like Airmon with leaves that exude a noxious vapor, leaving a trail of toxicity in its wake.",
            "rarity": RarityType.MYTHICAL,
            "type": AirmonType.H2S,
        },
        {
            "name": "Plastoxin",
            "description": "A sludge-like Airmon formed from industrial waste, its gelatinous body oozing with toxins and pollutants.",
            "rarity": RarityType.MYTHICAL,
            "type": AirmonType.H2S,
        },
        {
            "name": "Fumeroar",
            "description": "A lion-like Airmon with a mane made of smog. Its roar can release clouds of harmful pollutants.",
            "rarity": RarityType.MYTHICAL,
            "type": AirmonType.H2S,
        },
        {
            "name": "Nebulisk",
            "description": "A ghostly Pokémon with a misty body that emits harmful vapors. It haunts industrial areas, feeding on pollution.",
            "rarity": RarityType.MYTHICAL,
            "type": AirmonType.H2S,
        },
    ]


def get_airmons():
    return airmons
