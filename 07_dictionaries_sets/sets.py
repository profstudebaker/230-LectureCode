'''
SETS
- unordered collection of unique items
- no sense of position/order/indexing
- no key/value pair associations
- no duplicate items
- can only contain immutable items
syntax: { item, item, item, ... }
'''
# creating sets
# empty_set = {} # this will create a dictionary
empty_set = set()
fruits = {"apples","pears","oranges"}
print(empty_set)
print(fruits)

# add and remove from sets
fruits.add("avocado")
print(fruits)

fruits.remove("pears")
print(fruits)

# randomly pick something from a set
# and remove it
random_item = fruits.pop()
print(random_item)
print(fruits)

# set comparisons
users_netflix = {"murphystude","grandma","z123"}
users_hulu = {"theBachelor", "grandma","woo789"}
users_disney = {"grandma", "grandpa", "woo789"}

# users who are ONLY in the Netflix set
# and have no accounts on other platforms
print(users_netflix - users_hulu - users_disney)
# users who are ONLY on hulu but no other platform
print(users_hulu - users_disney - users_netflix)
# users who have an account on every single platform
print(users_netflix.intersection(users_hulu, users_disney))
# all users who have an account on any platform
print(users_disney.union(users_netflix, users_hulu))

if "grandma" in users_disney:
    print("Grandma has a Disney+ account.")
else:
    print("No account on Disney+ for grandma.")
