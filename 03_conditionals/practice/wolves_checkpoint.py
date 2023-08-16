# have to import modules before we use them
import math, random
# define our constants from the problem
HEIGHT = 12
BOW_RANGE = 15
# get the value from the user
distance = int(input("Enter distance of wolf (in feet): "))

hypot = math.sqrt((HEIGHT**2) + (distance**2))
print("You need a range of ", hypot, " feet.")
print("Your bow's range: ", BOW_RANGE)
"""
Add some random chance to your wolf game. 

If the wolf is in range, you should generate a number 
between 1 and 10 to use as the odds for a successful hit. 
Tell the user what their odds are 
(a 1 in 10 chance, a 3 in 10 chance, etc) 
and ask them if they want to shoot an arrow. 

If they do, implement your odds and tell the user 
whether or not they hit the wolf or missed.
"""
if hypot <= BOW_RANGE:
    print("Wolf is in range!")
    # WRITE YOUR CODE HERE
    # generate the odds between 1 and 10
    odds = random.randint(1, 10)
    # tell the user what their odds are
    print(f"You have a {odds}/10 chance of a hit.")
    # print("You have a ", odds, "/10 chance of a hit.")
    # ask the user if they want to shoot
    shoot_choice = input("Do you want to shoot an arrow? (y/n)")

    if shoot_choice == "y":
        # if so, generat another random number to use for the probability of hit or miss
        hit_number = random.randint(1, 10)
        if hit_number <= odds:
            # based on the second random number, print if hit or miss
            print("CRITICAL HIT!")
        else:
            print("You missed.")

    else:
        print("OK, you're waiting for a better opportunity.")

else:
    print("Wolf is NOT in range!")
