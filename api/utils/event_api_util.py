from .requester import Requester
from ..models import EventModel, EventCategoryModel


url = "https://culturify.azurewebsites.net/events/aire_lliure/"
client = Requester(url)


def update_event_data():
    pass
