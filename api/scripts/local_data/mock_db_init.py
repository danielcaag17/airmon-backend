
if __name__ == "__main__":
    from api.scripts.django_setup import setup_django

    setup_django()

    from api.scripts.local_data.load_air_data import load_air_data
    from api.scripts.local_data.create_airmons import load_air_data
    from api.utils.airmons_spawn import reset_spawns, spawn_new_airmons

    load_air_data()
    reset_spawns()
    spawn_new_airmons()