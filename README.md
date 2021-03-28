# yaledining [![PyPI version](https://badge.fury.io/py/yaledining.svg)](https://badge.fury.io/py/yaledining)

> Python library for obtaining Yale Dining data via the [YaleDine](https://yaledine.com) API.

NOTE: The legacy Yale Dining API has been deprecated and Yale is not updating the data it provides. As of v2, this package instead uses the [YaleDine](https://github.com/ErikBoesen/YaleDine) API, an unofficial student project that scrapes Yale's various dining websites and provides clean and standardized JSON-formatted menus.

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
api = yaledining.API()
# "api" name is just an example, this may be anything you desire
```

This API does not require authentication.

## Retrieval Functions
- `halls()`: get a list of all dining `Hall`s on campus.
- `hall(id)`: get a single `Hall` object by ID (two-letter abbreviation).
- `hall_managers(hall_id)`: get managers for a `Hall`.
- `hall_meals(hall_id, [date], [start_date], [end_date])`: get a list of `Meal` objects from a certain hall. Equivalent to `meals`, but with mandatory `hall_id`.
- `managers([hall_id]): get a list of `Manager` objects, from a single hall if specified or for all halls if not.
- `meals([hall_id], [date], [start_date], [end_date])`: get a list of `Meal` objects representing meals listed for the `hall_id` specified, or all halls if omitted. Specify `date` to get meals for a certain date, or `start_date` and `end_date` to get meals for an inclusive range of dates. Omit all three to get all meals.
- `meal(id)`: get single `Meal` by ID.
- `meal_items(meal_id)`: get a list of menu `Item`s included in a meal with given ID.
- `items([meal_id])`: get a list of `Item`s served in a given meal, or all items.
- `item_nutrition(item_id)`: get nutrition data for a menu item.

Note that it almost always cleaner to use builder syntax such as:
```py
meal = api.hall('GH').meals(datetime.date.today())[0]
item = meal.items[0]
item.nutrition.calories  # => 340
```
See more examples in `example.py`.

## Models
Models follow the schema listed in the [YaleDine API documentation](https://yaledine.com). Shortcut methods provided by this package are listed below for your convenience.

* `Hall`: a dining hall.
    * `managers`: get `Manager`s for this hall.
    * `meals([date], [start_date], [end_date])`: get `Meal`s in this hall, providing date parameters as in standard `meals` call.
* `Manager`: a manager for a hall, stored inside `Hall` objects.
* `Meal`: a single meal.
    * `items`: get menu `Item`s in this meal.
* `Item`: a single menu item.
    * `nutrition`: shortcut to get `Nutrition` for the item.
* `Nutrition`: index of nutrition facts for an `Item`.

See `example.py` for several usage examples.

## Author
[Erik Boesen](https://github.com/ErikBoesen)

This software is not endorsed by Yale Dining, Yale Hospitality, or Yale University.

## License
[GPL](LICENSE)
