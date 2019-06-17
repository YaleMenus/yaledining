class _base_model():
    def __init__(self, raw: dict, api):
        self.raw = raw
        self.api = api

    def __repr__(self):
        return '%s(%s)' % (self.__class__.__name__, self.raw)


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
        self.latitude, self.longitude = raw['GEOLOCATION'].split(',')
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
