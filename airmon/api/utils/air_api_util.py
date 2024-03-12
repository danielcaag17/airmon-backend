import pandas
from datetime import datetime
from .requester import Requester

url = "https://analisi.transparenciacatalunya.cat/resource/tasf-thgu.json"
client = Requester(url)


def request_air_data():
    """
    Requests air data from the air quality API
    """

    date = datetime.now()
    date = date.replace(hour=0, minute=0, second=0, microsecond=0)
    date = date.isoformat()
    data = pandas.DataFrame.from_records(client.get(limit=1000, where=f"data='{date}'"))

    print(data.to_dict(orient="records"))
