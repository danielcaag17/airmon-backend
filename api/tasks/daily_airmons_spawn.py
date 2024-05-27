from celery import shared_task
import logging

from api.utils.airmons_spawn import reset_spawns, spawn_new_airmons

logger = logging.getLogger(__name__)


@shared_task
def daily_airmons_spawn():
    reset_spawns()
    logger.info("reset_spawns executed successfully!")
    spawn_new_airmons()
    logger.info("spawn_new_airmons executed successfully!")
