# TODO: create a dictionary of pokemon (or other characters)
# with their type (fire/water/earth/etc)
# and an inner dictionary of moves 
# where each move has a min and max value of damage
import random
pokemon = {
    'pikachu': {
        'type': 'electric',
        'moves': {
            'blast': [3, 10],
            'zap': [5,7]
        }
    }, 
    'charmander': {
        'type': 'fire',
        'moves': {
            'flamethrower': [4, 10],
            'explosion': [8,10]
        }
    }
}
usersTurn = True 
available_pokemon = list(pokemon.keys())
computer = random.choice(available_pokemon)
health = [100, 100] # 0 for user, 1 for computer

# ask the user which pokemon they want to play
pokemon_selection = input(f"Which pokemon do you choose? ({available_pokemon})")

playing = True
while playing: 
    if usersTurn:
        # print out their moves and ask which move they want to play
        move_selection = input(f"Which move do you want to play? ({pokemon[pokemon_selection]['moves'].keys()})")
        # generate a random number between the min and max damage
        # of the selected move and print out how much damage occurred
        damage = random.randint(pokemon[pokemon_selection]['moves'][move_selection][0],pokemon[pokemon_selection]['moves'][move_selection][1])
        print(f"{move_selection} caused {damage} damage!")
        health[1] = health[1] - damage
    else:
        move_selection = random.choice(list(pokemon[computer]["moves"].keys()))
        print(f"Computer selected move {move_selection}")
        damage = random.randint(pokemon[computer]['moves'][move_selection][0],pokemon[computer]['moves'][move_selection][1])
        print(f"{move_selection} caused {damage} damage!")
        health[0] = health[0] - damage

    # print out the health of both pokemon
    print(f"Computer: {health[1]} | Player: {health[0]}")
    # change whose turn it is
    usersTurn = not usersTurn

