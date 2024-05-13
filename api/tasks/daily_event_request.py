from celery import shared_task
import logging

from ..utils import event_api_util

logger = logging.getLogger(__name__)


@shared_task
def daily_event_request():
    event_api_util.update_event_data()
    logger.info("Updated events information from the API successfully!")