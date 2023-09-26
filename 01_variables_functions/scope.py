'''
SCOPE
- Scope is the concept in programming of what names
  are defined in which sections of your code
- A variable is "in scope" if it currently is defined and has a value
  at the point you are trying to access it
- Python is friendly with "scope" so most of the time
  we don't have to think about it
- all variables in python have global scope, unless the variable is defined inside a function
- this is why we think of our functions as seperate from our main program
- as you get to more advanced programming languages, scope gets more complicated
'''

def different_scope(name_within_function):
    i_only_exist_here = 10
    print(name) # technically you can do this, but it is bad practice
    print(name_within_function) # taking all required values as params is better
    return i_only_exist_here

if __name__ == "__main__":
    # NameError: name 'i_only_exist_here' is not defined
    # print(i_only_exist_here)

    name = "Murphy" # defining here creates a variable with global scope
    different_scope()

    # if you want to access a variable outside of the function
    # where it was defined, you should return it
    result = different_scope()
    print(result)

