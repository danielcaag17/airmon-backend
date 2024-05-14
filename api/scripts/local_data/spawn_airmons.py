from api.scripts.django_setup import setup_django

setup_django()

from api.utils.airmons_spawn import reset_spawns, spawn_new_airmons  # noqa E402

reset_spawns()
spawn_new_airmons()
