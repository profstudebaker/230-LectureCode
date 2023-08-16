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
    print("You did not pick a valid number.")
    print(e)
except:
    # this is a general catch-all for any errors
    print("You did something else wrong.")


a = 10
b = 2

try:
  print(a/b)
except ZeroDivisionError:
  print("You can't divide by zero, silly!")
