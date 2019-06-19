# yaledining [![PyPI version](https://badge.fury.io/py/yaledining.svg)](https://badge.fury.io/py/yaledining)

> Python library for interfacing with the Yale Dining API.

[API documentation](https://developers.yale.edu/yale-dining)

## Guiding principles
This API seeks to enable Pythonic code using Yale Dining API data. For this reason, original names and unpleasant styles of data storage and access are often overridden.

For example:
- Names are put in standardized, Pythonic snake case (eg: `DININGLOCATIONNAME` becomes `dining_location_name`)
- Some clumsy naming is redone entirely (eg: locations' `ID_LOCATION` field simply is called `id` since the fact that it identifies a `Location` is implicit)
- More intuitive types are used, for example booleans over 0/1 integers
- `Location`'s `GEOLOCATION` property, while still accessible through `geolocation`, can be accessed through `latitude` and `longitude` propeties as well
- `Location` managers can be accessed as their own objects through the tuple `Location.managers`, with easier `name` and `email` properties
- Menu data from the API is split into `Meal` and `Item` objects to decrease data duplication and increase clarity
- `Meal` date and time fields use `datetime` and `time`

If you do **NOT** desire to use these enhancements, you may get the `raw` property of an object this wrapper returns:
```py
location = api.location('Branford')  # -> returns Location object
location.raw  # -> {'ID_LOCATION': '2', ... }
```
Doing so will get a dictionary of an object in similar format to how it's normally returned.

## Setup
First, install the module:

```sh
pip3 install yaledining
```

Then, to use these functions, you must import the module:

```py
import yaledining
```

Before using the library, you must instantiate its class, for example:

```py
api = yaledining.YaleDining()
# "api" name is just an example, this may be anything you desire
```

This API does not require authentication.

## Retrieval Functions
- `get_locations()`
- `get_menus(location_id)`
- `get_nutrition(item_id)`
- `get_traits(item_id)`
- `get_ingredients(item_id)`

See `example.py` for several usage examples.

## Author
[Erik Boesen](https://github.com/ErikBoesen)

## License
[GPL](LICENSE)
