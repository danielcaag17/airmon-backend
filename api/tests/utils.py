from django.contrib.auth.models import User
import pytz

from ..models import Airmon, Capture, Chat


def create_user(username):
    return User.objects.create_user(username=username)


def create_airmon(name):
    return Airmon.objects.create(name=name)


def create_capture(user, airmon, date, attempts):
    return Capture.objects.create(username=user, airmon=airmon, date=date, attempts=attempts)


def create_chat(user1, user2):
    return Chat.objects.create(user1=create_user(user1), user2=create_user(user2))


def get_timezone():
    return pytz.timezone("Europe/Madrid")
