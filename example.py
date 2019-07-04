import yaledining

# You can call this anything
api = yaledining.YaleDining()

# Test parameters obtained from API documentation.
locations = api.locations()
print('There are %d locations, the name of one of them is %s' % (len(locations), locations[5].name))
location = api.location('Grace Hopper')
print('%s is located at %s (latitude %f) and its phone number is %s.' % (location.name,
                                                                         location.address,
                                                                         location.latitude,
                                                                         location.phone))
print('It is ' + ('open' if location.open else 'closed'))
print('The first manager\'s email is ' + location.managers[0].email)
meals = location.meals
print('It has %d meals currently posted.' % len(meals))
for meal in meals:
    print(meal.name + ':')
    for item in meal.items:
        print('%s %s vegetarian' % (item.name, 'is' if item.traits.vegetarian else 'isn\'t'))
        ingredients = item.ingredients
        print('Has %d ingredients, the most significant of which is %s' % (len(ingredients), ingredients[0]))

# Or you can pass a menu item ID directly
print(api.traits(5908402))

# You can also search for locations by ID or name
print(api.location(1).name)
print(api.location('Slifka Center').open)
# By default, similar results will be matched as well
print(api.location('wést').name)  # "West Campus"
