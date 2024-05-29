from api.models.trophy_type import TrophyType


trophies = [
    {
        "name": "Caçador Mestre",
        "type": TrophyType.BRONZE,
        "description": "Captura Arimons per obtenir aquest trofeu",
        "requirement": 10,
        "xp": 200,
    },
    {
        "name": "Caçador Mestre",
        "type": TrophyType.PLATA,
        "description": "Captura Arimons per obtenir aquest trofeu",
        "requirement": 300,
        "xp": 9000,
    },
    {
        "name": "Caçador Mestre",
        "type": TrophyType.OR,
        "description": "Captura Arimons per obtenir aquest trofeu",
        "requirement": 2500,
        "xp": 75000,
    },
    # ------------------------------------------------------------------------------------------------------------------
    {
        "name": "Llibertador d’Esperits",
        "type": TrophyType.BRONZE,
        "description": "Allibera Arimons per obtenir aquest trofeu",
        "requirement": 5,
        "xp": 200,
    },
    {
        "name": "Llibertador d’Esperits",
        "type": TrophyType.PLATA,
        "description": "Allibera Arimons per obtenir aquest trofeu",
        "requirement": 200,
        "xp": 10000,
    },
    {
        "name": "Llibertador d’Esperits",
        "type": TrophyType.OR,
        "description": "Allibera Arimons per obtenir aquest trofeu",
        "requirement": 2000,
        "xp": 100000,
    },
    # ------------------------------------------------------------------------------------------------------------------
    {
        "name": "Col·leccionista quotidià",
        "type": TrophyType.BRONZE,
        "description": "Captura Arimons comuns per obtenir aquest trofeu",
        "requirement": 5,
        "xp": 75,
    },
    {
        "name": "Col·leccionista quotidià",
        "type": TrophyType.PLATA,
        "description": "Captura Arimons comuns per obtenir aquest trofeu",
        "requirement": 300,
        "xp": 5000,
    },
    {
        "name": "Col·leccionista quotidià",
        "type": TrophyType.OR,
        "description": "Captura Arimons comuns per obtenir aquest trofeu",
        "requirement": 3000,
        "xp": 60000,
    },
    # ------------------------------------------------------------------------------------------------------------------
    {
        "name": "Explorador Especial",
        "type": TrophyType.BRONZE,
        "description": "Captura Arimons especials per obtenir aquest trofeu",
        "requirement": 5,
        "xp": 100,
    },
    {
        "name": "Explorador Especial",
        "type": TrophyType.PLATA,
        "description": "Captura Arimons especials per obtenir aquest trofeu",
        "requirement": 250,
        "xp": 7500,
    },
    {
        "name": "Explorador Especial",
        "type": TrophyType.OR,
        "description": "Captura Arimons especials per obtenir aquest trofeu",
        "requirement": 2500,
        "xp": 80000,
    },
    # ------------------------------------------------------------------------------------------------------------------
    {
        "name": "Caçador Èpic",
        "type": TrophyType.BRONZE,
        "description": "Captura Arimons èpics per obtenir aquest trofeu",
        "requirement": 5,
        "xp": 150,
    },
    {
        "name": "Caçador Èpic",
        "type": TrophyType.PLATA,
        "description": "Captura Arimons èpics per obtenir aquest trofeu",
        "requirement": 100,
        "xp": 4500,
    },
    {
        "name": "Caçador Èpic",
        "type": TrophyType.OR,
        "description": "Captura Arimons èpics per obtenir aquest trofeu",
        "requirement": 1000,
        "xp": 50000,
    },
    # ------------------------------------------------------------------------------------------------------------------
    {
        "name": "Descobridor Mític",
        "type": TrophyType.BRONZE,
        "description": "Captura Arimons mítics per obtenir aquest trofeu",
        "requirement": 3,
        "xp": 200,
    },
    {
        "name": "Descobridor Mític",
        "type": TrophyType.PLATA,
        "description": "Captura Arimons mítics per obtenir aquest trofeu",
        "requirement": 50,
        "xp": 4000,
    },
    {
        "name": "Descobridor Mític",
        "type": TrophyType.OR,
        "description": "Captura Arimons mítics per obtenir aquest trofeu",
        "requirement": 250,
        "xp": 25000,
    },
    # ------------------------------------------------------------------------------------------------------------------
    {
        "name": "Llegenda Vivent",
        "type": TrophyType.BRONZE,
        "description": "Captura Arimons llegendaris per obtenir aquest trofeu",
        "requirement": 1,
        "xp": 500,
    },
    {
        "name": "Llegenda Vivent",
        "type": TrophyType.PLATA,
        "description": "Captura Arimons llegendaris per obtenir aquest trofeu",
        "requirement": 10,
        "xp": 5000,
    },
    {
        "name": "Llegenda Vivent",
        "type": TrophyType.OR,
        "description": "Captura Arimons llegendaris per obtenir aquest trofeu",
        "requirement": 50,
        "xp": 50000,
    },
    # ------------------------------------------------------------------------------------------------------------------
    {
        "name": "Apostador Aeri",
        "type": TrophyType.BRONZE,
        "description": "Fes tirades a la ruleta diaria per obtenir aquest trofeu",
        "requirement": 1,
        "xp": 100,
    },
    {
        "name": "Apostador Aeri",
        "type": TrophyType.PLATA,
        "description": "Fes tirades a la ruleta diaria per obtenir aquest trofeu",
        "requirement": 30,
        "xp": 4000,
    },
    {
        "name": "Apostador Aeri",
        "type": TrophyType.OR,
        "description": "Fes tirades a la ruleta diaria per obtenir aquest trofeu",
        "requirement": 100,
        "xp": 15000,
    },
    # ------------------------------------------------------------------------------------------------------------------
    {
        "name": "Alquimista de Combat",
        "type": TrophyType.BRONZE,
        "description": "Utilitza consumibles per obtenir aquest trofeu",
        "requirement": 20,
        "xp": 1000,
    },
    {
        "name": "Alquimista de Combat",
        "type": TrophyType.PLATA,
        "description": "Utilitza consumibles per obtenir aquest trofeu",
        "requirement": 200,
        "xp": 10000,
    },
    {
        "name": "Alquimista de Combat",
        "type": TrophyType.OR,
        "description": "Utilitza consumibles per obtenir aquest trofeu",
        "requirement": 2000,
        "xp": 100000,
    },
    # ------------------------------------------------------------------------------------------------------------------
    {
        "name": "Comprador Compulsiu",
        "type": TrophyType.BRONZE,
        "description": "Realitza compres per obtenir aquest trofeu",
        "requirement": 25,
        "xp": 500,
    },
    {
        "name": "Comprador Compulsiu",
        "type": TrophyType.PLATA,
        "description": "Realitza compres per obtenir aquest trofeu",
        "requirement": 200,
        "xp": 4500,
    },
    {
        "name": "Comprador Compulsiu",
        "type": TrophyType.OR,
        "description": "Realitza compres per obtenir aquest trofeu",
        "requirement": 2500,
        "xp": 50000,
    },
    # ------------------------------------------------------------------------------------------------------------------
    {
        "name": "Rei del Tresor",
        "type": TrophyType.BRONZE,
        "description": "Guanya monedes per obtenir aquest trofeu",
        "requirement": 500,
        "xp": 500,
    },
    {
        "name": "Rei del Tresor",
        "type": TrophyType.PLATA,
        "description": "Guanya monedes per obtenir aquest trofeu",
        "requirement": 5000,
        "xp": 5000,
    },
    {
        "name": "Rei del Tresor",
        "type": TrophyType.OR,
        "description": "Guanya monedes per obtenir aquest trofeu",
        "requirement": 1000000,
        "xp": 1000000,
    },
]


def get_trophies():
    i = 3
    for trophy in trophies:
        trophy["name"] = "trophy" + str(int(i/3))
        trophy["description"] = "descTrophy" + str(int(i/3))
        i += 1
    return trophies
