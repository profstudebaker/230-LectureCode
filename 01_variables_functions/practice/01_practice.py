"""
Write a program that gets 2 numbers 
from a user and then prints out 
their sum and their product.
"""
# get a number from user input
# make sure it's a number (not a string)


# num1 = int(input("Enter a number: "))
# # get another number (same thing)
# num2 = int(input("Enter another number: "))
# print("You entered ", num1, "and", num2)
# # find the sum
# print("Sum: ", int(num1) + int(num2))
# # find the product
# print("Product: ", num1 * num2)

"""
Write a program that gets 
the user’s monthly budget for restaurants 
and the average cost of a meal. 
Print out how many times a week 
they can eat at a restaurant.
""" 
# ask for monthly budget - float
monthly_budget = float(input("Enter monthly budget: "))
# ask for average cost of meal - float
avg_meal = float(input("Enter average cost of a meal: "))
# get the weekly budget by dividing monthly by 4
weekly_budget = monthly_budget / 4
# divide weekly budget by the average cost
meals_per_week = weekly_budget // avg_meal
# print that result out
print("You can afford " ,meals_per_week, "meals per week")

"""
PROBLEM 1
Write a program that gets 2 numbers from a user and then prints out their sum and their product.
"""
# use the input() function to get values from user
# INPUT IS ALWAYS A STRING so we must type-cast it to an int
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

# to print both strings and numeric types, we can use commas
print("You entered ", num1, "and", num2)
# or we can type-cast the numeric type to a string
print("Sum: " + str(num1 + num2))
print("Product: " + str(num1 * num2))
"""
PROBLEM 2
Write a program that gets the user’s monthly budget for restaurants and the average cost of a meal. Print out how many times a week they can eat at a restaurant.
"""
# same thing, we need to cast our input to the appropriate type
monthly_budget = float(
    input("How much can you spend per month on restaurants? "))
# we use a float here because an average cost of something
# could likely be a floating point number (i.e. $12.75)
avg_meal = float(input("What's the average cost of a meal where you live? "))
# the // operator calculates floor division
# which will round down to the nearest whole number
# we do this so you don't have fractions of meals (silly)
# we divide by 4 to get budget per week
meals = (monthly_budget / 4) // avg_meal

print("You can afford", meals, "meals a week.")
"""
PROBLEM 3
Write a program that gets the cost of a drink and prints out the total bill including tax and tip. Assume that the tax rate is 8% and the tipping rate is 20%.
"""
# here we get to use constants, because things like tax rate
# and tip rate we are assuming will stay the same
TAX_RATE = .08
TIPPING_RATE = .2

# we use a float again because money typically has 2 decimal points
cost = float(input("Enter cost of drink: "))
total_cost = (cost * TAX_RATE) + (cost * TIPPING_RATE) + cost
# we will learn more about how to format output later
print("Your drink will actually cost $" + str(total_cost))
"""
PROBLEM 4
Ask the user for the total minutes of screen time they spent on their phone yesterday (you can usually find this in settings on Androids and iPhones — if not, estimate the number). 

Assuming that trend stays the same daily, print out the total minutes of screen time they’ll spend on their phone in a week, month, and year.
"""
screen_time = int(input("Enter daily minutes of screen time: "))
print("You will spend", screen_time * 7, " minutes a week on your phone.")
print("You will spend", screen_time * 30, " minutes a month on your phone.")
print("You will spend", screen_time * 365, " minutes a year on your phone.")
