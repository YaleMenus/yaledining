import requests


class ConnectionError(Exception):
    """Raised when an error occurs in connecting to the API."""
    pass


class YaleDining:
    API_ROOT = 'http://www.yaledining.org/fasttrack/'
    API_VERSION = 3

    def __init__(self):
        pass

    def get(self, endpoint: str, make_list: bool = True, params: dict = {}):
        """
        Make a GET request to the dining API.

        :param endpoint: path to resource desired.
        :param make_list: should data be restructured into a list of dictionaries for easier manipulation?
        :param params: dictionary of custom params to add to request.
        """
        custom_params = {
            'version': seelf.API_VERSION,
        }
        custom_params.update(params)
        request = requests.get(self.API_ROOT + endpoint, params=custom_params)
        if request.ok:
            data = request.json()
            if make_list:
                data = [
                    {data['COLUMNS'][index]: entry[index] for index in range(len(entry))}
                    for entry in data['DATA']
                ]
            return data
        else:
            # TODO: Can we be more helpful?
            raise ConnectionError('API request failed.')