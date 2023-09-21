"""
Print out a menu to the user 
asking them if they want an inspirational quote, 
song lyric, or affirmation. Based on their choice, 
print out the appropriate response.
"""
# print("""
# --~* Menu *~--
# 1) Inspirational Quote
# 2) Song Lyric
# 3) Affirmation
# """)
# # show the user what options they can make
# choice = int(input("Make a selection (1/2/3):"))
# theme = "star wars"
# if choice == 1 and theme == "star wars":
#     # print out an inspirational quote
#     print("Do or do not. There is no try. -Yoda")
# elif choice == 1:
#     # we know the theme is something else because the theme was not star wars
#     print("Just do it! -Nike")
# elif choice == 2:
#     # chose song lyric
#     print("song lyric")
# elif choice == 3:
#     print("You LOVE to participate in class!")
# else:
#     # tell them they did not choose an item from the menu
#     print("Invalid selection.")

"""
MODULES
- think of these as expansion packs for python
- you need to import them at the top of the file by convention
- some are built in to python and some you can download and install
(spotify, googlemaps, sklearn)
"""
# have to import the modules before you use them
# best practice is to put this at the very top of your file
import random, math

MIN = 1
MAX = 100
# generate a random number between min and max with randint()
# (both min and max are inclusive)
# generate a num between 1 and 100
random_number = random.randint(MIN, MAX)
print(f"Computer generated #{random_number}")

"""
Groundhog Day Program
30% odds that the groundhog sees his shadow
70% odds that the groundhog does not see his shadow
"""
# generate a number between 1 and 10
number = random.randint(1,10)
if number <= 3: # 3 is threshold
    # true if number is 1,2, or 3
    print("Groundhog sees shadow!")
else: 
    # true if number is 4,5,6,7,8,9, or 10
    print("Groundhog does not see shadow.")

word = "HANGMAN"
# we want to generate a hint to the user
# by selecting a random letter from the word
hint = random.choice(word) # will choose one item from the collection passed in
print("Hint: " + hint)

print(math.sqrt(25))

