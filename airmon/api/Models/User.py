from django.db import models


class Usuari (models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=16)
    idioma = models.CharField(max_length=100)
    dataRegistre = models.DateTimeField(auto_now_add=True)
    ultimAcces = models.DateTimeField(auto_now=True)