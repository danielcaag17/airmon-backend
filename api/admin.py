from django.contrib import admin
from django.apps import apps
from .models import BannedPlayer
# Register your models here.

# Register models
admin.site.register(BannedPlayer)

