def spawn_airmons():
    from api.utils.airmons_spawn import reset_spawns, spawn_new_airmons  # noqa E402

    reset_spawns()
    spawn_new_airmons()


if __name__ == "__main__":
    from api.scripts.django_setup import setup_django

    setup_django()
    spawn_airmons()
