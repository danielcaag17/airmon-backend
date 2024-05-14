from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=32, primary_key=True)
    price = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='items/')
    duration = models.TimeField(default=0)
