from api.scripts.django_setup import setup_django
setup_django()

from api.utils.air_api_util import update_air_data

update_air_data()