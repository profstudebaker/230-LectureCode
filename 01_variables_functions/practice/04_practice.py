
"""
PROBLEM 4
Ask the user for the total minutes of screen time they spent on their phone yesterday (you can usually find this in settings on Androids and iPhones — if not, estimate the number). 

Assuming that trend stays the same daily, print out the total minutes of screen time they’ll spend on their phone in a week, month, and year.
"""
screen_time = int(input("Enter daily minutes of screen time: "))
print("You will spend", screen_time * 7, " minutes a week on your phone.")
print("You will spend", screen_time * 30, " minutes a month on your phone.")
print("You will spend", screen_time * 365, " minutes a year on your phone.")
