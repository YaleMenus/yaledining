class _base_model(dict):
    def __init__(self, raw: dict, api):
        self.update(json)
        self.update(self.__dict__)
        self.__dict__ = self
        self.api = api

    def __repr__(self):
        return '%s(%s)' % (self.__class__.__name__, self.json())

    def json(self):
        return dict.__repr__(self)

    def raw(self):
        return dict(self)


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
    @property
    def managers(self):
        """
        Get a list of managers in an easily manipulable format.

        :return: list of Manager objects.
        """
        managers = []
        num_managers = 0
        while num_managers < 4:
            num_managers += 1

            manager = (location[f'MANAGER{num_managers}NAME'],
                       location[f'MANAGER{num_managers}EMAIL'])
            if manager == (None, None):
                break
            managers.append(manager)
        return managers
