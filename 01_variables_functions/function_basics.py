'''
DEFINING OUR OWN FUNCTIONS
- like we learned last class, functions are a named set of operations that take in input and produce some output (most of the time)
- some functions are built into the python language, but we can also define our own
- in general, functions should always return the same value for the same set of parameters
- functions help us write "clean code" for a number of reasons:
  a) they allow you to take a bunch of statements and group them together and give them a name, keeping your code more organized 
  b) they allow you to re-use code you've written instead of copy and pasting
  c) they allow you to "abstract away" complex code from your main program body, creating code that is easier for another developer to read and understand
  d) there is only one place to debug something that isn't working properly
  e) you can import functions into other programs and re-use them across multiple projects or with teams of developers
'''

# DEFINING FUNCTIONS
# we can define our own functions by using the keyword "def"
# then specifying our function's name and what input values
# our function expects


# in this piece of code, we have defined a function named "generate_greeting"
# that accepts one paramater named "name"
# and returns a string value representing a greenting to that name
def generate_greeting(name):
    return "Howdy, " + name + "!"


# CALLING FUNCTIONS
# a function definition is just a definition
# to actually run the code, you have to call the function
# when you call a function, you pass in "arguments"
# for each expected parameter value
# since our function only defined one parameter, we pass in one argument
print(generate_greeting("Partner"))
# above we are printing out the returned value from our function
# we could also save it to a variable and then print it or do something else with it
greeting = generate_greeting("Partner")
print(greeting)
# we could even get some input from the user and pass that in to our function
name = input("What is your name? ")
print(generate_greeting(name))


# PARAMETER DEFAULTS
# you can have as many params as you want
# and you can also set a default value for a param,
# which will be used if no argument is passed in for that param
# all parameters with defaults should be listed at the end
def generate_greeting(name, greeting="Howdy"):
    return greeting + ", " + name + "!"


# now, if we only pass in a value for name, the greeting will always be "Howdy"
print(generate_greeting(name))
# but if we pass in a name and a greeting to our function call
# we override the default value
print(generate_greeting(name, "Hiya there"))
print(generate_greeting(name, "heyyy"))
print(generate_greeting(name, "What's crack-a-lacking"))


