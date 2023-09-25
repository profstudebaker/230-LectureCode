import random

"""
LOOPS
- allow you to repeat chunks of code multiple times
- come in two flavors: for and while, choose which one based on problem
- keyword break stop the loop completely
- keyword continue skips to the next iteration of the loop
"""
"""
WHILE LOOPS
- keep running as long as a condition is true
- be careful not to have an infinite loop
- can do anything a for loop can, but with less happening automatically
"""
number = random.randint(1,10)
guess = int(input("Guess a number between 1 and 10: "))
print("Generated: " + str(number))
while guess != number: # keep allowing user to guess until they get it right
  print("Wrong!")
  guess = int(input("Guess a number between 1 and 10: "))
print("CORRECT!")

"""
FOR LOOPS
- commonly used to go through every item in a collection
- use range() function if you want a pre-determined amount of times
- use enumerate() if you want access to the iteration count and the value of the item
"""
hand = [2, 2, 4, 10]
# find the highest card in your hand
# by looping through each card and keeping track of 
# whether or not it is higher than the last card
max_card = hand[0] # set to first card
for card in hand: 
  # "card" is a new variable that is automatically 
  # given the value of the current item
  if card > max_card:
    # found a new max card!
    max_card = card
print(max_card)

# USING RANGE
number = random.randint(1,10)
print("Generated: " + str(number))
for guess in range(3): # allow the user to make 3 guesses
  guess = int(input("Guess a number between 1 and 10: "))
  if guess == number:
    print("You got it!")
    break # they got it right, so stop the loop
  else: 
    print("Incorrect.")

# USING ENUMERATE
hand = [2, 2, 4, 10]
# find the highest card in your hand
# by looping through each card and keeping track of 
# whether or not it is higher than the last card
max_card = hand[0] # set to first card
max_position = 0
for position, card in enumerate(hand): 
  # "card" is a new variable that is automatically 
  # given the value of the current item
  print(f"Evaluating position {position}. Value: {card}")
  if card > max_card:
    # found a new max card!
    max_card = card
    max_position = position