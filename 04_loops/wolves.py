# have to import modules before we use them
import math, random
# define our constants from the problem
HEIGHT = 12
BOW_RANGE = 15
WOLVES = 6
ARROWS = 10
game_play = True
# get the value from the user
#distance = int(input("Enter distance of wolf (in feet): "))
distance = 3
hypot = math.sqrt((HEIGHT**2) + (distance**2))
print("You need a range of ", hypot, " feet.")
print("Your bow's range: ", BOW_RANGE)

while game_play:
    if hypot <= BOW_RANGE:
        print("Wolf is in range!")
        # generate the odds between 1 and 10
        odds = random.randint(1, 10)
        # tell the user what their odds are
        print(f"You have a {odds}/10 chance of a hit.")
        # ask the user if they want to shoot
        shoot_choice = input("Do you want to shoot an arrow? (y/n)")

        if shoot_choice == "y":
            ARROWS -= 1 # decrement arrows
            # if so, generat another random number to use for the probability of hit or miss
            hit_number = random.randint(1, 10)
            if hit_number <= odds:
                # based on the second random number, print if hit or miss
                print("CRITICAL HIT!")
                WOLVES -= 1 # decrement wolves
            else:
                print("You missed.")

        else:
            print("OK, you're waiting for a better opportunity.")
    else: 
        print("The wolf is NOT in range!")

    print(f"""
    Wolves: {WOLVES} | Arrows: {ARROWS}
    """)
    if WOLVES == 0 or ARROWS == 0:
        game_play = False
        # or use break here

print(f"""
------ GAME OVER -------
Wolves: {WOLVES} | Arrows: {ARROWS}
""")
if WOLVES == 0:
    print("You are a champion!")
elif ARROWS == 0:
    print("You have been eaten by wolves...")