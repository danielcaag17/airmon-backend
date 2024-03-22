# tasks.py

from celery import shared_task
import logging

logger = logging.getLogger(__name__)


@shared_task
def mock_task():
    # Add your mock functionality here
    logger.info("Mock task executed successfully!")
