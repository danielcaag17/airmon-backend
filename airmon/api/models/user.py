from django.contrib.auth.hashers import make_password, check_password
from django.db import models

from airmon.api.models.language import Language


class User (models.Model):
    username = models.CharField(max_length=32, primary_key=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=16)
    language = models.CharField(max_length=16, choices=[(tag, tag.value) for tag in Language])
    # Amb auto_now_add es registrara la data i hora en el mateix moment que es crei el registre
    register_date = models.DateTimeField(auto_now_add=True)
    # Amb auto_now es registrara la data i hora quan es faci una modificacio en el registre
    last_access = models.DateTimeField(auto_now=True)

    def set_password(self, password):
        # Guarda la contrasenya de forma segura amb bcrypt
        self.password = make_password(password)

    def check_password(self, password):
        # Verifica si la contrasenya donada coincideix amb el hash guardat
        return check_password(password, self.password)
