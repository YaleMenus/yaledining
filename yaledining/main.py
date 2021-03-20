import requests
import datetime
from unidecode import unidecode
from .models import *


class ConnectionError(Exception):
    """Raised when an error occurs in connecting to the API."""
    pass


class YaleDining:
    def __init__(self):
        raise Exception('The YaleDining class has been deprecated in v2.0 of this package. Use API instead.')


class API:
    API_ROOT = 'https://yaledine.com/api/'
    DATE_FMT = '%Y-%m-%d'

    def get(self, endpoint: str, params: dict = {}, json=True):
        """
        Make a GET request to the API.

        :param endpoint: path to resource desired.
        :param params: dictionary of custom params to add to request.
        """
        request = requests.get(self.API_ROOT + endpoint, params=params)
        if request.ok:
            return request.json()
        else:
            raise ConnectionError('API request failed.')

    def _date(self, raw):
        if type(raw) == str:
            return raw
        if type(raw) in (datetime.date, datetime.datetime):
            return raw.strftime(self.DATE_FMT)
        return None

    def halls(self):
        """
        Get all halls available from the API.
        """
        return [Hall(raw, self) for raw in self.get('halls')]

    def hall(self, id: str):
        """
        Get a single dining hall by ID.
        :param id: ID (two-letter abbreviation) of the hall you want.
        """
        return Hall(self.get(f'hall/{id}', self))

    def meals(self, hall_id: str = None, date=None, start_date=None, end_date=None):
        """
        Get meals for a given hall (or all halls if hall_id is omitted), for a given date or within a range.
        :param hall_id: ID (two-letter abbreviation) of hall for which to get menus.
        :param date: single date to get meals for. Can be YYYY-MM-DD string or datetime.date.
        :param start_date: start of date range to get meals for. Ignored if date is passed. Can be YYYY-MM-DD string or datetime.date.
        :param end_date: end of date range to get meals for. Ignored if date is specified. Can be YYYY-MM-DD string or datetime.date.
        """
        endpoint = f'halls/{hall_id}/meals' if hall_id else 'meals'
        params = {}
        if date:
            params['date'] = self._date(

        # Dictionary mapping date strings to dictionaries mapping meal names to lists of items
        days = {}
        for raw_item in raw:
            date = raw_item['MENUDATE']
            meal_code = raw_item['MEALCODE']
            item = Item(raw_item, self)
            if date not in days:
                days[date] = {}
            if meal_code not in days[date]:
                days[date][meal_code] = Meal(raw_item, self)
            days[date][meal_code].items.append(item)
        meals = []
        for day in days:
            for meal in days[day]:
                meals.append(days[day][meal])
        return meals

    def nutrition(self, item_id: int):
        """
        Get nutrition data for a menu item.
        :param item_id: ID of item to get data on.
        """
        return Nutrition(self.get('menuitem-nutrition.cfm', params={'MENUITEMID': item_id})[0], self)

    def traits(self, item_id: int):
        """
        Get traits data of a menu item, for example whether it's vegetarian, whether it contains pork, nuts, etc.
        :param item_id: ID of item to get data on.
        """
        return Traits(self.get('menuitem-codes.cfm', params={'MENUITEMID': item_id})[0], self)

    def ingredients(self, item_id: int):
        """
        Get a list of ingredients of a menu item.
        :param item_id: ID of item to get data on.
        :return: list of string-format ingredient names, in descending order of prevalence.
        """
        return [raw['INGREDIENT'] for raw in self.get('menuitem-ingredients.cfm', params={'MENUITEMID': item_id})]
