from django.db import models


class Usuari (models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=16)
    idioma = models.CharField(max_length=100)
    dataRegistre = models.DateTimeField(auto_now_add=True)
    ultimAcces = models.DateTimeField(auto_now=True)


class Jugador (Usuari):   # Hereda Usuari
    puntsXP = models.IntegerField()
    monedes = models.IntegerField()
    ubicacioActualX = models.IntegerField()
    ubicacioActualY = models.IntegerField()


class Caputra (models.Model):
    nombreIntents = models.IntegerField()
    horaCaptura = models.DateTimeField()


class Item (models.Model):
    nom = models.CharField(max_length=100)
    # raresa = models.IntegerField()
    preu = models.IntegerField()
    descripcio = models.IntegerField()


class ItemEnPropietat (models.Model):
    quantitat = models.IntegerField()



