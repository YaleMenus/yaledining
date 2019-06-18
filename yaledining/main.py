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

    def get(self, endpoint: str, make_list: bool = True, params: dict = {}):
        """
        Make a GET request to the dining API.

        :param endpoint: path to resource desired.
        :param make_list: should data be restructured into a list of dictionaries for easier manipulation?
        :param params: dictionary of custom params to add to request.
        """
        custom_params = {
            'version': self.API_VERSION,
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

    def locations(self):
        return [Location(raw, self) for raw in self.get('locations.cfm')]

    def _lenient_equals(self, a, b):
        a = unidecode(a.lower())
        b = unidecode(b.lower())
        if a == b: return True
        a = a.split()[0]
        b = b.split()[0]
        if a == b: return True
        return False

    def location(self, id: int = None, name: str = None, lenient_matching: bool = True):
        for location in self.locations():
            if id is not None:
                # Then Freud was right all along
                if location.id == id:
                    return location
            elif name is not None:
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
