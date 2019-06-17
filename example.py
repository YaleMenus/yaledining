import yaledining

dining = yaledining.YaleDining()

# Test parameters obtained from API documentation.
print(dining.get_locations())
print(dining.get_menus(location_id=3))
print(dining.get_nutrition(item_id=5908402))
print(dining.get_traits(item_id=5908402))
print(dining.get_ingredients(item_id=5908402))
