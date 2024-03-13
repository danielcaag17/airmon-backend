import pandas
from datetime import datetime
from .requester import Requester
from ..data_providers.provider_registry import provider_registry

provider = provider_registry.get_provider(name="gen_cat")

if provider.url is None:
    raise ValueError("No provider found")

client = Requester(provider.url)


def request_air_data():
    """
    Requests air data from the air quality API
    """

    date = datetime.now()
    date = date.replace(hour=0, minute=0, second=0, microsecond=0)
    date = date.isoformat()
    data = pandas.DataFrame.from_records(client.get(limit=1000, where=f"data='{date}'"))

    return data.to_dict(orient="records")
