import yaledining
import datetime

# You can call this anything
api = yaledining.API()

# Test parameters obtained from API documentation.
halls = api.halls()
print('There are %d halls, the name of one of them is %s' % (len(halls), halls[5].name))
hall = api.hall('GH')
print('%s is located at %s (latitude %f) and its phone number is %s.' % (hall.name,
                                                                         hall.address,
                                                                         hall.latitude,
                                                                         hall.phone))
print('It is ' + ('open' if hall.open else 'closed'))
print('The first manager\'s email is ' + hall.managers[0].email)
meals = hall.meals(date=datetime.date.today())
print('It has %d meals posted today.' % len(meals))
for meal in meals:
    print('-' * 10)
    print(meal.name + ':')
    for item in meal.items:
        print('%s %s contain meat' % (item.name, 'does' if item.meat else 'doesn\'t'))
        print('Its ingredients are ' + item.ingredients)
        nutrition = item.nutrition
        print('One serving is %s, and contains %d calories.' % (nutrition.serving_size, nutrition.calories))
