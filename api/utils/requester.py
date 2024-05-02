import requests

methods = ["GET"]


def remove_empty_fields(args):
    result = {}
    for param in args:
        if args[param] is not None:
            result[param] = args[param]
    return result


class Requester:

    def __init__(
            self,
            url,
            username=None,
            password=None,
            app_token=None,
            timeout=10,
    ):
        """
        The Requester class is a simple class that takes an url and allows
        to make requests to that url following the Socrata (SoQL) language

        The url param is necessary
        """
        if not url:
            raise Exception("url cannot be empty")
        self.url = url

        self.session = requests.Session()
        # We can add basic http auth here if needed
        # Requests will be limited to get otherwise

        if not isinstance(timeout, (int, float)):
            raise Exception("timeout must be a number")
        self.timeout = timeout

    def get(self, **kwargs):
        """
        Read data from the requested resource. Options for content_type are json,
        csv, and xml. Optionally, specify a keyword arg to filter results:

            select : the set of columns to be returned, defaults to *
            where : filters the rows to be returned, defaults to limit
            order : specifies the order of results
            group : column to group results on
            limit : max number of results to return, defaults to 1000
            offset : offset, used for paging. Defaults to 0
            q : performs a full text search for a value
            query : full SoQL query string, all as one parameter
            exclude_system_fields : defaults to true. If set to false, the
                response will include system fields (:id, :created_at, and
                :updated_at)

        More information about the SoQL parameters can be found at the official
        docs:
            http://dev.socrata.com/docs/queries.html

        More information about system fields can be found here:
            http://dev.socrata.com/docs/system-fields.html
        """

        params = {
            "$select": kwargs.pop("select", None),
            "$where": kwargs.pop("where", None),
            "$order": kwargs.pop("order", None),
            "$group": kwargs.pop("group", None),
            "$limit": kwargs.pop("limit", None),
            "$offset": kwargs.pop("offset", None),
            "$q": kwargs.pop("q", None),
            "$query": kwargs.pop("query", None),
            "$$exclude_system_fields": kwargs.pop("exclude_system_fields", None),
        }

        params = remove_empty_fields(params)

        return self.perform_request("GET", params=params)

    def perform_request(self, method, **kwargs):
        if method not in methods:
            raise Exception("Invalid method")

        kwargs["timeout"] = self.timeout

        response = self.session.request(method, self.url, **kwargs)

        if response.status_code not in (200, 202):
            raise Exception(
                f"Request failed with status code {response.status_code}"
            )

        if not response.text:
            return response

        return response.json()

    def __enter__(self):
        return self

    def __exit__(self, exc_type=None, exc_value=None, traceback=None):
        """
        This runs at the end of a with block. It simply closes the client.

        Exceptions are propagated forward in the program as usual, and
            are not handled here.
        """
        self.close()

    def close(self):
        """
        Closes the client.
        """
        self.session.close()
