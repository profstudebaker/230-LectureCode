"""
PROBLEM 3
Write a function that accepts the cost of a drink as a parameter 
and returns the total bill including tax and tip. 
Assume that the tax rate is 8% and the tipping rate is 20%.
"""
# let's make a function!
# this will allow us to reuse this code for multiple
# different costs
def calculate_drink_cost(initial_cost):
    # here we get to use constants, because things like tax rate
    # and tip rate we are assuming will stay the same
    TAX_RATE = .08
    TIPPING_RATE = .2
    # we use a float again because money typically has 2 decimal points
    total_cost = (initial_cost * TAX_RATE) + (initial_cost * TIPPING_RATE) + initial_cost
    return total_cost

###################################
cost = float(input("Enter cost of drink: "))
total = calculate_drink_cost(cost)
# we will learn more about how to format output later
print(f"Your drink will actually cost ${total:.2f}")
# print(total)