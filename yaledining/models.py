import datetime


class _base_model:
    def __init__(self, raw: dict, api):
        self.raw = raw
        for key in raw:
            setattr(key, raw[key])
        self.api = api



class Hall(_base_model):
    @property
    def meals(self):
        return self.api.meals(self.id)


class Manager(_base_model):
    pass



class Meal(_base_model):
    @property
    def items(self):
        return self.api.items(self.id)


class Item(_base_model):
    @property
    def nutrition(self):
        """
        Get nutrition information for the current item.
        """
        return self.api.nutrition(self.id)


class Nutrition(_base_model):
    pass
