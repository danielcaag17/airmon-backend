
def load_air_data():
    from api.utils.air_api_util import update_air_data

    update_air_data()

if __name__ == "__main__":
    from api.scripts.django_setup import setup_django

    setup_django()
    load_air_data()
