from django.db import models

from .rarity_type import RarityType


class Item (models.Model):
    name = models.CharField(max_length=32, primary_key=True)
    rarity = models.CharField(max_length=32, choices=RarityType.choices, default=RarityType.COMU)
    price = models.DecimalField(decimal_places=2, max_digits=7)
    description = models.TextField()

    def save(self, *args, **kwargs):
        if n_decimals(self.price) > 2:
            self.price = round(self.price, 2)
            super().save(*args, **kwargs)
        elif self.rarity not in [choice[0] for choice in RarityType.choices]:
            raise ValueError(f"Invalid rarity value. {self.rarity}")
        else:
            super().save(*args, **kwargs)


# Calcular el número de decimals que té price
def n_decimals(price):
    price_str = str(price)

    if '.' in price_str:
        # Trobar la posició del punt decimal
        posicion_decimal = price_str.index('.')

        # Contar els digits després del punt
        num_decimales = len(price_str) - posicion_decimal - 1
        return num_decimales
    else:
        # Si no hi ha punt decimal, el preu no te decimals
        return 0
