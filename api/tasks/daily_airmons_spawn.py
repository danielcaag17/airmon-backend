from celery import shared_task

from api.utils.airmons_spawn import reset_spawns, spawn_new_airmons

@shared_task
def daily_airmons_spawn():
    reset_spawns()
    spawn_new_airmons()
