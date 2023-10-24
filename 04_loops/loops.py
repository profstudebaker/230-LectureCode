import random
"""
LOOPS
- allow you to repeat chunks of code
- come in two flavors: for and while, you want to choose the right loop for the job
- break stops the loop completely
- continue skips to the next iteration
- when you're starting out, it is helpful to draw out variables on paper
"""

'''
WHILE LOOPS
- keep running as long as a condition is true
- be careful of infinite looping
'''

# create a number guessing game
# that generates a random number between 1 and 10
# keeps asking the user to guess the number 
# until the user gets it right

# number = random.randint(1, 10)
# print("Generated ", number)
# guess = int(input("Guess a number between 1 and 10: "))
# while guess != number: 
#     # ask them to guess again
#     guess = int(input("Guess again: "))
# print("Correct!")

'''
FOR LOOPS
- typically used to run for a pre-determined amount of times
- the loop variable changes depending on what you are looping through
'''
MAX_GUESSES = 3
# adapt the number guessing program
# so that the user only has MAX_GUESSES chances to guess
# print out how many guesses are remaining
# and then stop if they get it right
number = random.randint(1,10)
print("Generated: ", number)
for i in range(MAX_GUESSES): # i will be 0, 1, 2
    # i is how many times we have guessed
    print(f"You have {MAX_GUESSES-i} guesses remaining.")
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == number:
        print("You are so so smart!")
        break
    
'''
NESTED LOOPS
- you can nest however many you want, like if statements
- want to be careful with spacing
- the innermost loop runs for each time the outer loop runs
  wait for inner loop to complete before next iteration of outer loop
'''
seats = "LMNOP"
num_rows = 3
# print out theatre seats: 1L 1M 1N 1O 1P, 2L 2M ... etc
for row in range(num_rows): # row will be 0, 1, 2
    for seat in seats: # seat will be L, M, N, O, P
        print(f"{row+1}{seat}")
    print("----------")