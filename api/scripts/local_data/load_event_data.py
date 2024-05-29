def load_event_data():
    from api.utils.event_api_util import update_event_data

    update_event_data()

if __name__ == "__main__":
    from api.scripts.django_setup import setup_django

    setup_django()
    load_event_data()
