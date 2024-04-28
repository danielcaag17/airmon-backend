from django.contrib.auth.models import User

from ..models import Airmon, Capture


def create_user(username):
    return User.objects.create_user(username=username)


def create_airmon(name):
    return Airmon.objects.create(name=name)


def create_capture(user, airmon, date, attempts):
    return Capture.objects.create(username=user, airmon=airmon, date=date, attempts=attempts)