"""
MODULES
- think of as "expansion packs"
- some modules are built in to python
(don't have to install)
- some are third party libraries 
(you do have to install, googlemaps, spotify, sklearn)
"""
# have to import any modules we are going to use
# by convention, we import all modules at the top
# import random, math 

# generate a number between 1 and 100
MIN = 1
MAX = 100
# use the randint() method
# first parameter is lower bound (inclusive)
# second param is upper bound (inclusive)
random_num = random.randint(MIN, MAX)
print(random_num)

# word = "EPITOME"
# # choose a random item from a sequence
# # a string is a sequence of characters
# hint = random.choice(word)
# print("Here's a hint: " + hint)

# # math module
# # gives you methods for common calculations
# # gives you some mathematical constants
# print(math.pi)

import math

monthly_budget = 400
avg_meal = 22.74
# could round with // (floor division)
n_meals = (monthly_budget / 4) / avg_meal
n_meals_round_down = math.floor(n_meals)
n_meals_round_up = math.ceil(n_meals)
print("Around ",n_meals_round_up, "per week.")

