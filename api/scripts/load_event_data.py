from api.scripts.django_setup import setup_django

setup_django()

from api.utils.event_api_util import update_event_data

update_event_data()
