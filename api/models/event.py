from django.db import models


class EventCategoryModel(models.Model):
    name = models.CharField(primary_key=True, max_length=32)


class EventModel(models.Model):
    codi = models.CharField(primary_key=True, max_length=32)
    # denominacio = models.TextField()
    descripcio = models.TextField()
    data_ini = models.DateTimeField()
    data_fi = models.DateTimeField()
    category = models.ForeignKey(EventCategoryModel, on_delete=models.CASCADE)
    # TODO: geohash OR location
    imatge = models.ImageField(upload_to='events/')
    entrades = models.TextField()
    espai = models.TextField()
