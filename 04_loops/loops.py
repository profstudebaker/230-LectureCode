import random
"""
FOR LOOPS


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


"""
WHILE LOOPS
"""
number = random.randint(1,10)
guess = int(input("Guess a number between 1 and 10: "))
print("Generated: " + str(number))
while guess != number: 
  print("Wrong!")
  guess = int(input("Guess a number between 1 and 10: "))
print("CORRECT!")