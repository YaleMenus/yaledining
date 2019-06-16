# tbapy [![PyPI version](https://badge.fury.io/py/yaledining.svg)](https://badge.fury.io/py/yaledining)

> Python library for interfacing with the Yale Dining API.

[API documentation](https://developers.yale.edu/yale-dining)

## Setup
First, install the module:

    pip3 install yale_dining

Then, to use these functions, you must import the `tbapy` module:

```py
import yale_dining
```

Before using the library, you must instantiate its class, for example:

```py
dining = yale_dining.YaleDining()
```

This API does not require authentication.

The Blue Alliance's API requires that all applications identify themselves with an auth key when retrieving data. To obtain an auth key, visit TBA's [Account page](https://www.thebluealliance.com/account).


## Retrieval Functions
You may specify `simple=True` to get only vital data on some models or lists of models, or you may specify `keys=True` to get a list of the keys for a list rather than full data on each model. It is recommended to use these options if you do not need full data.

Some requests support `year` and other optional parameters, which are recommended to use to narrow down your results.
* `tba.status()` - Get TBA's status.
* `tba.teams([page], [year], [simple/keys])` - Get a list of of valid teams, where `page * 500` is the starting team number. If no page is provided, all teams will be fetched.
* `tba.team(team, [simple])` - Get a team's data. `team` can be an integer team number of a string-form `'frc####'` identifier.

See `example.py` for several usage examples.

## Author
[Erik Boesen](https://github.com/ErikBoesen)

## License
[GPL](LICENSE)
