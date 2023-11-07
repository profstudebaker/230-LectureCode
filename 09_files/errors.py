'''
Exception Handling
- our code should run without any errors when given the expected input
from users or from files (this is our job to ensure as developers)
- occasionally, we might anticipate some malicious/invalid input
that would cause our working code to fail and give an error
- exception handling allows us to anticipate these failures and 
handle them within our code how we see fit

There are four different keyword blocks when using exception handling
- most will only use try/except
- but you can also use else and finally 

- You can check for multiple different kinds of errors
- Python will check for these similar to an if statement
in order from the top to the bottom, so more specific or critical
errors should be handled first
'''


'''
Using error checking to verify the type of a user input.
'''
user_input = input("Enter a number: ")
try:
  # attempts to run
  user_input = int(user_input)
except:
  # runs if exception
  print("That was not a number.")
else:
  # runs if no exception
  print("Thanks for following instructions!")
finally:
  # runs no matter what
  print("~ program aborting ~")
  

'''
You can put this in a loop to continue prompting the user
until they follow instructions
'''
while True:
    user_input = input("Please enter an integer: ")
    try:
        user_input = int(user_input)
        break  # Break out of the loop if the input is a valid integer
    except ValueError:
        print("Invalid input. Please enter an integer.")

print("You entered:", user_input)

 
'''
Using error checking to prevent common errors when getting user input/reading from a file/etc. 
'''
fruits = ['apple', 'banana', 'pear', 'orange']
selection = input("Enter which number of fruit you want: ")
try:
    selection = int(selection)
    selected_fruit = fruits[selection]
    print("You picked " + selected_fruit)
except ValueError as e:
    # we can specify different except blocks
    # for different types of errors
    # we want to order Errors more specific -> less specific
    print("You did not enter a number.")
    print(e)
except IndexError as e:
    print("Your number did not correspond to a fruit.")
    print(e)
except:
    # this is a general catch-all for any errors
    print("You did something else wrong.")


a = 10
b = 0

try:
  print(a/b)
except ZeroDivisionError:
  print("You can't divide by zero, silly!")
