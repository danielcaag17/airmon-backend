from api.scripts.django_setup import setup_django
from api.utils.event_api_util import update_event_data

setup_django()

update_event_data()
