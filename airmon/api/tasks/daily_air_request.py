# tasks.py

from celery import shared_task
import logging

from ..utils import air_api_util

logger = logging.getLogger(__name__)


@shared_task
def daily_air_request():
    air_api_util.update_air_data()
    logger.info("Updated air information from the API successfully!")
