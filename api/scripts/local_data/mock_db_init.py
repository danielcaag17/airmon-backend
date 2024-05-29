def mock_db_init():
    from api.scripts.local_data.load_air_data import load_air_data
    from api.scripts.local_data.create_airmons import create_airmons
    from api.scripts.local_data.fill_spawn_points import populate_barcelona_spawn_points
    from api.utils.airmons_spawn import reset_spawns, spawn_new_airmons
    from api.scripts.local_data.create_trophies import create_trophies
    from api.scripts.local_data.populate_items import populate_items

    load_air_data()
    create_airmons()
    populate_barcelona_spawn_points()
    reset_spawns()
    spawn_new_airmons()
    create_trophies()
    populate_items()


if __name__ == "__main__":
    from api.scripts.django_setup import setup_django

    setup_django()

    mock_db_init()
