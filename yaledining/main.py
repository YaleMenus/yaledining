import requests
from unidecode import unidecode
from .models import *


class ConnectionError(Exception):
    """Raised when an error occurs in connecting to the API."""
    pass


class YaleDining:
    API_ROOT = 'http://www.yaledining.org/fasttrack/'
    API_VERSION = 3

    def __init__(self):
        pass

    def get(self, endpoint: str, params: dict = {}):
        """
        Make a GET request to the dining API.

        :param endpoint: path to resource desired.
        :param params: dictionary of custom params to add to request.
        """
        custom_params = {
            'version': self.API_VERSION,
        }
        custom_params.update(params)
        request = requests.get(self.API_ROOT + endpoint, params=custom_params)
        if not request.ok:
            raise ConnectionError('API request failed.')
        data = request.json()
        # Restructure data into a list of dictionaries for easier manipulation
        data = [
            {data['COLUMNS'][index]: entry[index] for index in range(len(entry))}
            for entry in data['DATA']
        ]
        return data

    def locations(self):
        return [Location(raw, self) for raw in self.get('locations.cfm')]

    def _lenient_equals(self, a, b):
        # These two comparisons should be split up because of locations whose names start with "Café"
        a = unidecode(a.lower())
        b = unidecode(b.lower())
        if a == b: return True
        a = a.split()[0]
        b = b.split()[0]
        if a == b: return True
        return False

    def location(self, identifier, lenient_matching: bool = True):
        """
        Get a single location by name or ID.

        :param identifier: numerical ID or name of location. If an integer is passed or a string that could be converted to
                           an integer, it will be assumed to be an ID. Otherwise, a location will be searched for by name.
        :param lenient_matching: if a name is provided, should close matches be tolerated as well?
        """
        if type(identifier) == str and identifier.isdigit():
            identifier = int(identifier)
        for location in self.locations():
            if type(identifier) == int:
                if location.id == identifier:
                    return location
            else:
                if location.name == name or lenient_matching and self._lenient_equals(location.name, name):
                    return location
        return None

    def menus(self, location_id: int):
        return [Menu(raw, self) for raw in self.get('menus.cfm', params={'location': location_id})]

    def nutrition(self, item_id: int):
        return Nutrition(self.get('menuitem-nutrition.cfm', params={'MENUITEMID': item_id})[0], self)

    def traits(self, item_id: int):
        return Traits(self.get('menuitem-codes.cfm', params={'MENUITEMID': item_id})[0], self)

    def ingredients(self, item_id: int):
        return [Ingredient(raw, self) for raw in self.get('menuitem-ingredients.cfm', params={'MENUITEMID': item_id})]
