import yaledining

dining = yaledining.YaleDining()

# Test parameters obtained from API documentation.
location = dining.locations()[0]
print('%s is located at %s (latitude %f) and its phone number is %s.' % (location.name,
                                                                         location.address,
                                                                         location.latitude,
                                                                         location.phone))
print('It is ' + ('open' if location.open else 'closed'))
print('The first manager\'s email is ' + location.managers[0].email)
menus = location.menus
"""
print('It has %d menus currently posted.' % len(menus))
for menu in menus:
    print('Is this menu vegetarian? ' + 'Yes' if menu.traits.vegetarian else 'No')
"""

# Or you can pass a menu item ID directly
print(dining.traits(5908402))

# You can also search for locations by ID or name
print(dining.location(1).name)
print(dining.location('Slifka Center').open)
# By default, similar results will be matched as well
print(dining.location('wést').name)  # "West Campus"

location = dining.location('Pierson')
location.menus
