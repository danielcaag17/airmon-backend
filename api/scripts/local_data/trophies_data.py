from api.models.trophy_type import TrophyType


trophies = [
    {
        "name": "Caçador Mestre",
        "type": TrophyType.BRONZE,
        "description": "Captura Arimons per obtenir aquest trofeu",
        "requirement": 10,
        "xp": 10,
    },
    {
        "name": "Caçador Mestre",
        "type": TrophyType.PLATA,
        "description": "Captura Arimons per obtenir aquest trofeu",
        "requirement": 25,
        "xp": 30,
    },
    {
        "name": "Caçador Mestre",
        "type": TrophyType.OR,
        "description": "Captura Arimons per obtenir aquest trofeu",
        "requirement": 50,
        "xp": 60,
    },
    # ------------------------------------------------------------------------------------------------------------------
    {
        "name": "Llibertador d’Esperits",
        "type": TrophyType.BRONZE,
        "description": "Allibera Arimons per obtenir aquest trofeu",
        "requirement": 5,
        "xp": 20,
    },
    {
        "name": "Llibertador d’Esperits",
        "type": TrophyType.PLATA,
        "description": "Allibera Arimons per obtenir aquest trofeu",
        "requirement": 10,
        "xp": 50,
    },
    {
        "name": "Llibertador d’Esperits",
        "type": TrophyType.OR,
        "description": "Allibera Arimons per obtenir aquest trofeu",
        "requirement": 25,
        "xp": 100,
    },
    # ------------------------------------------------------------------------------------------------------------------
    {
        "name": "Col·leccionista quotidià",
        "type": TrophyType.BRONZE,
        "description": "Captura Arimons comuns per obtenir aquest trofeu",
        "requirement": 5,
        "xp": 5,
    },
    {
        "name": "Col·leccionista quotidià",
        "type": TrophyType.PLATA,
        "description": "Captura Arimons comuns per obtenir aquest trofeu",
        "requirement": 20,
        "xp": 20,
    },
    {
        "name": "Col·leccionista quotidià",
        "type": TrophyType.OR,
        "description": "Captura Arimons comuns per obtenir aquest trofeu",
        "requirement": 50,
        "xp": 50,
    },
    # ------------------------------------------------------------------------------------------------------------------
    {
        "name": "Explorador Especial",
        "type": TrophyType.BRONZE,
        "description": "Captura Arimons especials per obtenir aquest trofeu",
        "requirement": 5,
        "xp": 10,
    },
    {
        "name": "Explorador Especial",
        "type": TrophyType.PLATA,
        "description": "Captura Arimons especials per obtenir aquest trofeu",
        "requirement": 20,
        "xp": 40,
    },
    {
        "name": "Explorador Especial",
        "type": TrophyType.OR,
        "description": "Captura Arimons especials per obtenir aquest trofeu",
        "requirement": 50,
        "xp": 100,
    },
    # ------------------------------------------------------------------------------------------------------------------
    {
        "name": "Caçador Èpic",
        "type": TrophyType.BRONZE,
        "description": "Captura Arimons èpics per obtenir aquest trofeu",
        "requirement": 5,
        "xp": 15,
    },
    {
        "name": "Caçador Èpic",
        "type": TrophyType.PLATA,
        "description": "Captura Arimons èpics per obtenir aquest trofeu",
        "requirement": 20,
        "xp": 60,
    },
    {
        "name": "Caçador Èpic",
        "type": TrophyType.OR,
        "description": "Captura Arimons èpics per obtenir aquest trofeu",
        "requirement": 50,
        "xp": 150,
    },
    # ------------------------------------------------------------------------------------------------------------------
    {
        "name": "Descobridor Mític",
        "type": TrophyType.BRONZE,
        "description": "Captura Arimons mítics per obtenir aquest trofeu",
        "requirement": 5,
        "xp": 20,
    },
    {
        "name": "Descobridor Mític",
        "type": TrophyType.PLATA,
        "description": "Captura Arimons mítics per obtenir aquest trofeu",
        "requirement": 20,
        "xp": 80,
    },
    {
        "name": "Descobridor Mític",
        "type": TrophyType.OR,
        "description": "Captura Arimons mítics per obtenir aquest trofeu",
        "requirement": 50,
        "xp": 200,
    },
    # ------------------------------------------------------------------------------------------------------------------
    {
        "name": "Llegenda Vivent",
        "type": TrophyType.BRONZE,
        "description": "Captura Arimons llegendaris per obtenir aquest trofeu",
        "requirement": 5,
        "xp": 25,
    },
    {
        "name": "Llegenda Vivent",
        "type": TrophyType.PLATA,
        "description": "Captura Arimons llegendaris per obtenir aquest trofeu",
        "requirement": 20,
        "xp": 100,
    },
    {
        "name": "Llegenda Vivent",
        "type": TrophyType.OR,
        "description": "Captura Arimons llegendaris per obtenir aquest trofeu",
        "requirement": 50,
        "xp": 250,
    },
    # ------------------------------------------------------------------------------------------------------------------
    {
        "name": "Apostador Aeri",
        "type": TrophyType.BRONZE,
        "description": "Fes tirades a la ruleta diaria per obtenir aquest trofeu",
        "requirement": 1,
        "xp": 10,
    },
    {
        "name": "Apostador Aeri",
        "type": TrophyType.PLATA,
        "description": "Fes tirades a la ruleta diaria per obtenir aquest trofeu",
        "requirement": 5,
        "xp": 25,
    },
    {
        "name": "Apostador Aeri",
        "type": TrophyType.OR,
        "description": "Fes tirades a la ruleta diaria per obtenir aquest trofeu",
        "requirement": 10,
        "xp": 50,
    },
    # ------------------------------------------------------------------------------------------------------------------
    {
        "name": "Alquimista de Combat",
        "type": TrophyType.BRONZE,
        "description": "Utilitza consumibles per obtenir aquest trofeu",
        "requirement": 1,
        "xp": 20,
    },
    {
        "name": "Alquimista de Combat",
        "type": TrophyType.PLATA,
        "description": "Utilitza consumibles per obtenir aquest trofeu",
        "requirement": 5,
        "xp": 50,
    },
    {
        "name": "Alquimista de Combat",
        "type": TrophyType.OR,
        "description": "Utilitza consumibles per obtenir aquest trofeu",
        "requirement": 10,
        "xp": 100,
    },
    # ------------------------------------------------------------------------------------------------------------------
    {
        "name": "Comprador Compulsiu",
        "type": TrophyType.BRONZE,
        "description": "Realitza compres per obtenir aquest trofeu",
        "requirement": 10,
        "xp": 50,
    },
    {
        "name": "Comprador Compulsiu",
        "type": TrophyType.PLATA,
        "description": "Realitza compres per obtenir aquest trofeu",
        "requirement": 25,
        "xp": 125,
    },
    {
        "name": "Comprador Compulsiu",
        "type": TrophyType.OR,
        "description": "Realitza compres per obtenir aquest trofeu",
        "requirement": 50,
        "xp": 250,
    },
    # ------------------------------------------------------------------------------------------------------------------
    {
        "name": "Rei del Tresor",
        "type": TrophyType.BRONZE,
        "description": "Guanya monedes per obtenir aquest trofeu",
        "requirement": 10,
        "xp": 10,
    },
    {
        "name": "Rei del Tresor",
        "type": TrophyType.PLATA,
        "description": "Guanya monedes per obtenir aquest trofeu",
        "requirement": 50,
        "xp": 50,
    },
    {
        "name": "Rei del Tresor",
        "type": TrophyType.OR,
        "description": "Guanya monedes per obtenir aquest trofeu",
        "requirement": 100,
        "xp": 100,
    },
]


def get_trophies():
    return trophies
