import requests
from .models import *


class ConnectionError(Exception):
    """Raised when an error occurs in connecting to the API."""
    pass


class YaleDining:
    API_ROOT = 'http://www.yaledining.org/fasttrack/'
    API_VERSION = 3

    def get(endpoint, version=3, make_list=True, params={}):
        custom_params = {
            'version': version,
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
            # TODO: actually say what's wrong
            raise Exception
