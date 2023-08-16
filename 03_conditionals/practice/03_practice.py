"""
Print out a menu to the user 
asking them if they want an inspirational quote, 
song lyric, or affirmation. Based on their choice, 
print out the appropriate response.
"""
# by using numbers in our menu design,
# we take away some of the ambiguity 
# and make for a better UX (User Experience)
MENU = """
--------- Menu ----------
1 - Inspirational Quote
2 - Song Lyric
3 - Affirmation
"""
print(MENU)
# we give the user a hint for the expected input format
# we don't need to cast to an int
# because we aren't doing any calculations
# just checking for equality
choice = input("Choose an option (1/2/3): ")
print("User selected ", choice)

# we can add an "or"
# to account for both the numerical
# or the textual representation
if (choice == "1" or choice == "Inspirational Quote"):
    print("There can't be a rainbow without a little bit of rain.")
elif (choice == "2"):
    print("Don't Stop Believing!")
elif (choice == "3"):
    print("You are a coding badass!")
else: 
    print("Invalid input.")


"""
Ask the user for the day of their birth (not month or year, just the day), then print out a fortune for them based on if their birth date is even or odd.
"""
day = int(input("On what day were you born? "))
# see if something is even by using %
# if it cannot be divided by 2 without a remainder, it is an odd number
if day % 2 == 0:
  # it's an even number
  print("My friend, your future is bright!")
else:
  # it's an odd number
  print("THE GRIM! THE GRIM! *drops teacup*")


"""
Ask the user for their midterm score (as an integer from 0→100), then print out the letter grade representation of their score.
"""
score = float(input("What was your midterm score? "))

# we want to use a bunch of ifs and elifs here
# best to start with the most specific option first
if score >= 90:
  print("A")
elif score >= 80:
  print("B")
elif score >= 70:
  print("C")
elif score >= 60:
  print("D")
else:
  print("F")


"""
Use random module to write a groundhog day program. 
You should implement a 30% probability 
that the groundhog will see his own shadow.
"""
import random
# generate a number between the range of possible outcomes
randy = random.randint(1, 10)
print("Generated ", randy)

# using that number, see if it is within
# a certain threshold based on the probability
if randy < 4:
  # 3 in 10 chance this is true
  print("Groundhog saw his own shadow!")
else: 
  # 7 in 10 chance this is true
  print("Groundhog did NOT see his own shadow.")

print(f"Random number was {randy}")