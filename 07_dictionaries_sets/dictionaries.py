import random
# """
# DICTIONARIES
# - associative data structure 
# (rather than sequential like a list or tuple)
# - stores key value pairs

# Think of an actual dictionary: 
# - the word is the key
# - the definition is the value

# Rules of a Dictionary
# - cannot have duplicate keys
# - keys should be immutable
# - values can basically be whatever 
# (can have duplicates, can have lists, can have nested dictionaries)
# - designed to be one way lookups key -> value
# its possible to get the key for a given value but it is 
# more difficult
# """
# # creating empty dictionary
# empty_dict = {}
# # creating populated dictionary
# # name_of_dict = {
# #    key : value,
# #    key : value, 
# # }
# state_capitals = {
#     'TX' : 'Austin',
#     'NY' : 'Albany',
#     'CA' : 'Sacramento'
# }
# print(state_capitals)
# grades = {
#     "Hermione Granger": ['A','A','A'],
#     "Ronald Weasley": ['F','D','F']
# }
# print(grades)

# # adding to a dictionary
# # use the key to index the dictionary
# # set the value for that key
# # name_of_dictionary[new_key] = new_value
# state_capitals['MI'] = 'Lansing'
# print(state_capitals)

# # updating a value in a dictionary
# # since TX is already a key in our dictionary,
# # python knows to update it instead of add another TX key
# # (because you cannot have duplicate keys)
# state_capitals['TX'] = 'Marfa'


# # accessing a value by key
# capital_of_new_york = state_capitals['NY']
# print(capital_of_new_york)

# # looping through keys
# for key in state_capitals:
#     print(f"Key: {key}")
#     print(f"Value: {state_capitals[key]}")

# # looping through values
# for val in state_capitals.values():
#     if 's' in val:
#         print(val + " has an a in it!")

# # looping through the key/val pairs
# for pair in state_capitals.items():
#     print(pair)
#     if 'Albany' in pair:
#         key_for_albany = pair[0]
#         print(key_for_albany)

# for key, val in state_capitals.items():
#     if val == 'Albany':
#         key_for_albany = key
#         print(key_for_albany)

# # check if a key exists in a dictionary 
# # KeyError means the key you used does not exist
# grades["Neville Longbottom"] = ['B','B','A']
# if "Neville Longbottom" in grades:
#     print(grades["Neville Longbottom"])
# else:
#     print("No record for this student.")
# # check if a value is present in the dictionary
# if ['A','A','A'] in grades.values():
#     print("We have a straight A student!")

# # data is often represented as a dictionary of dictionaries
# # where each outer key is a row's ID
# # and the inner dictionary's keys are the column names
# # mapping to the value for that row
# players = {
#     'James': {
#         'type': 'Wizard',
#         'level': 3,
#         'health': 80
#     },
#     'Larry': {
#         'type': 'Warrior',
#         'level': 1,
#         'health': 10
#     },
#     'Julia': {
#         'type': 'Giant',
#         'level': 12,
#         'health': 95
#     }
# }

# # you then index a given value by providing two key
# print(players['Julia']['type'])
# print(players['Larry']) # all of Larry's stats
# print(players['James']['health'])

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

computer = 'charmander'
user = 'pikachu'

moves_options_computer = list(pokemon[computer]["moves"].keys())
print(moves_options_computer)
computers_move = random.choice(moves_options_computer)
print(f"Computer chose {computers_move}")
min_damage = pokemon[computer]["moves"][computers_move][0]
max_damage = pokemon[computer]["moves"][computers_move][1]
damage = random.randint(min_damage, max_damage)
print(f"Computer caused {damage} damage!")
