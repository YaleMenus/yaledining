import yaledining

dining = yaledining.YaleDining()

# Test parameters obtained from API documentation.
location = dining.get_locations()[0]
print('%s is located at %s (latitude %f) and its phone number is %s.' % (location.name,
                                                                         location.address,
                                                                         location.latitude,
                                                                         location.phone))
print('It is ' + ('open' if location.open else 'closed'))
print('The first manager\'s email is ' + location.managers[0].email)

'''
print(dining.get_menus(location_id=3))
print(dining.get_nutrition(item_id=5908402))
print(dining.get_traits(item_id=5908402))
print(dining.get_ingredients(item_id=5908402))
'''
