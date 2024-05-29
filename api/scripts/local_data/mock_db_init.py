def mock_db_init():
    from api.scripts.local_data.load_air_data import load_air_data
    from api.scripts.local_data.create_airmons import create_airmons
    from api.scripts.local_data.fill_spawn_points import populate_barcelona_spawn_points
    from api.scripts.local_data.spawn_airmons import spawn_airmons
    from api.scripts.local_data.load_event_data import load_event_data
    from api.scripts.local_data.populate_items import populate_items
    from api.scripts.local_data.create_trophies import create_trophies
    from api.scripts.local_data.demo import create_demo_user

    load_air_data()
    load_event_data()
    create_airmons()
    populate_barcelona_spawn_points()
    spawn_airmons()
    populate_items()
    create_trophies()
    create_demo_user()


if __name__ == "__main__":
    from api.scripts.django_setup import setup_django

    setup_django()

    mock_db_init()
