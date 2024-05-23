import datetime
from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=32, primary_key=True)
    price = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='items/', default='items/default.png')
    duration = models.TimeField(default=datetime.time())
