"""
PROBLEM 2
Write a program that gets the user’s monthly budget for restaurants 
and the average cost of a meal. Print out how many times a week 
they can eat at a restaurant.
"""
# same thing, we need to cast our input to the appropriate type
monthly_budget = float(input("How much can you spend per month on restaurants? "))
# we use a float here because an average cost of something
# could likely be a floating point number (i.e. $12.75)
avg_meal = float(input("What's the average cost of a meal where you live? "))
# the // operator calculates floor division
# which will round down to the nearest whole number
# we do this so you don't have fractions of meals (silly)
# we divide by 4 to get budget per week
meals = (monthly_budget / 4) // avg_meal

print("You can afford", int(meals), "meals a week.")