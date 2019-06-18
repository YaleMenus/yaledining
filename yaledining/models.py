import datetime


class _base_model():
    def __init__(self, raw: dict, api):
        self.raw = raw
        self.api = api

    def __repr__(self):
        return '%s(%s)' % (self.__class__.__name__, self.raw)

    def parse_datetime(self, raw: str) -> datetime.datetime:
        return datetime.strptime(raw, '%B, %e %Y %H:%M:%S')

    def parse_time(self, raw: str):
        return datetime.strptime(raw, '%H:%M %p').time()


def _make_model(class_name):
    return type(class_name, (_base_model,), {})


class Manager:
    """
    A manager for a dining location.

    Built at request time to make processing/iteration easier.
    """
    def __init__(self, name, email):
        self.name = name
        self.email = email


class Location(_base_model):
    def __init__(self, raw: dict, api):
        super().__init__(raw, api)
        self.id = int(raw['ID_LOCATION'])
        self.location_code = int(raw['LOCATIONCODE'])
        self.name = raw['DININGLOCATIONNAME']
        # TODO: enum?
        self.type = raw['TYPE']
        self.capacity = raw['CAPACITY']
        self.percent_capacity = 10 * self.capacity if self.capacity is not None else None
        self.geolocation = raw['GEOLOCATION']
        self.latitude, self.longitude = tuple([float(coordinate) for coordinate in raw['GEOLOCATION'].split(',')])
        self.closed = bool(raw['ISCLOSED'])
        self.open = not self.closed
        self.address = raw['ADDRESS']
        self.phone = raw['PHONE']
        managers = []
        num_managers = 0
        while num_managers < 4:
            num_managers += 1
            name = raw[f'MANAGER{num_managers}NAME']
            email = raw[f'MANAGER{num_managers}EMAIL']
            if name is not None and email is not None:
                managers.append(Manager(name, email))
        self.managers = tuple(managers)


class Menu(_base_model):
    def __init__(self, raw: dict, api):
        super().__init__(raw, api)
        self.location_id = int(raw['ID_LOCATION'])
        self.location_code = int(raw['LOCATIONCODE'])
        self.location_name = raw['LOCATION']
        self.meal_name = raw['MEALNAME']
        self.meal_code = int(raw['MEALCODE'])
        # Dates are formatted like:
        # June, 18 2019 00:00:00
        # TODO: should we provide the string format as well?
        self.raw_date = raw['MENUDATE']
        self.date = datetime.strptime(self.raw_date, '%B, %e %Y %H:%M:%S')
        self.id = int(raw['ID'])
        self.course = raw['COURSE']
        self.course_code = int(float(raw['COURSECODE']))
        self.item = raw['MENUITEM']
        self.item_id = int(float(raw['MENUITEMID']))
        # TODO: What is this?
        self.is_par = bool(raw['ISPAR'])
        # Times formatted like:
        # 08:00 AM
        self.raw_open_time = raw['MEALOPENS']
        self.open_time = self.parse_time(self.raw_open_time)
        self.raw_close_time = raw['MEALCLOSES']
        self.close_time = self.parse_time(self.raw_close_time)
        self.is_default_meal = bool(raw['ISDEFAULTMEAL'])
        self.is_menu = bool(raw['ISMENU'])
