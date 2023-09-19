"""
Print out a menu to the user 
asking them if they want an inspirational quote, 
song lyric, or affirmation. Based on their choice, 
print out the appropriate response.
"""
print("""
~*~ Menu ~*~
1 - Quote
2 - Song Lyric
3 - Affirmation
""")
choice = int(input("Select an option (1/2/3): "))

if choice == 1:
    # print out an inspirational quote
    print("Do or do not, there is no try. - Yoda")
elif choice == 2:
    print("Never gonna give you up!!!!!")
elif choice == 3:
    print("Love yourself! Believe in YOURSELF!!")
else: 
    print("You made an invalid selection.")

"""
MODULES
- think of them as expansion packs for python
- you import them and then you can use a bunch of exciting functions
- some modules you can download from the internet and install
(spotify, googlemaps, sklearn)
"""
# typically we always import modules at the top of our files
import math, random

# generate random numbers with randint() method
# pass in two parameters - lower bound, upper bound
MIN = 1
MAX = 5
random_num = random.randint(MIN, MAX)
# print(f"Computer Generated ~|{random_num}|~")

# groundhog day program 
# 30% odds that groundhog will see his shadow
# 70% odds that groundhog will not see his sahdow
number = random.randint(1, 10)
print("Generated", number)
if number <= 3: # 1 2 or 3
    print("Groundhog will see his shadow.")
else: # 4,5,6,7,8,9, or 10
    print("Groundhog will not see his shadow.")


word = "HANGMAN"
# choose a random letter from this word
# to show the user as a hint
hint = random.choice(word)
print("Here is a hint: " + hint)

print(math.sqrt(25))
