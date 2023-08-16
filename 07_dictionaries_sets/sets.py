'''
SETS
- unordered collection of unique items
- there is no sense of position (like a list)
- sets cannot hold duplicate items
- not key/value pairs like a dictionary 
- can only contain immutable values
- { item, item, item }
'''
# create an empty set
empty_set = set()
# empty_set = {} # DO NOT DO THIS!!! THIS IS A DICTIONARY
print(type(empty_set))

# create a populated set
fruits = {'apple','pear','banana'}
print(fruits)

# sets do not have to be homogenous 
mixed_sets = { 4, "4", True}
print(mixed_sets)

# items in a set have to be immutable
# set_of_lists = {[4,5],[1,1]}
# print(set_of_lists)
set_of_tuples = {(4,5),(1,1)}
print(set_of_tuples)

# adding to a set
fruits.add("tomato")
print(fruits)

# remove items from a set by value
fruits.remove("tomato")
print(fruits)

# remove a random item 
popped = fruits.pop()
print(popped)
print(fruits)

# set comparisons
users_netflix = {"murphystude","grandma","z123"}
users_hulu = {"theBachelor","grandma","woo789"}
users_disney = {"grandma","grandpa"}

# users who are ONLY in the netflix set
print(users_netflix - users_hulu)
# users who are ONLY in the hulu set
print(users_hulu - users_netflix)
# users who have accounts on both platforms
print(users_hulu.intersection(users_netflix).intersection(users_disney))
# users who have an account on either platform
print(users_netflix.union(users_hulu))

# check if a value is present in a set
if "pear" in fruits:
    print("It's a fruit!")
else: 
    print("It's not a fruit!")


