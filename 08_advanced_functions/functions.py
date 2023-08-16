'''
Write a void function called yell 
that takes in a message
and prints out that message in uppercase
with 5 exclamation points at the end.
'''
def yell(message, n_exclamations=5):
    exclamations = ""
    for n in range(n_exclamations):
        exclamations += "!"
    print(message.upper() + exclamations)

# to run the function, we have to call it
yell("CPSC230 is my favorite class")
# yell("golden retrievers are the best dogs")
user_input = input("Enter a message: ")
yell(user_input, 10)


'''
Write a function to implement a random chance of death
that takes in the probability of dying
and returns True if the player died
and False if the player survived
'''
import random
def random_death(probability):
    random_number = random.randint(0,100)
    if random_number < probability:
        return True # player died
    else:
        return False # player survived

if random_death(0):
    print("GAME OVER!")
else:
    print("You have entered the chamber of secrets.....")