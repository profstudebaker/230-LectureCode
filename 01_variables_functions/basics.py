'''
BASICS
- every piece of code is just a text file, programming languages allow us to write instructions in human-readable language that the computer understands how to translate into machine code and execute
- different programming languages are optimized for different tasks, python is generally understood to be best for ease of use/learning and as a "jack of all trades" language
- syntax will change between languages, but many of the concepts we will learn will be the same in any programming language
'''
# EXPRESSIONS, VARIABLES, STATEMENTS
# an expression is a piece of code that evaluates to a value
3 + 6  # evaluates to 9

# a variable is a named entity used to store a value
# we can assign a direct value to a variable
year = 2023
# or we can assign an expression to the variable
# whatever the expression evaluates to at the time
# it is run will be the value assigned to the variable
# if you change the value of "year" the value of "last_year"
# would also change
last_year = year - 1

# an entire instruction of code is called a statement
# in line 19, we wrote a statement that assigns the value of
# the variable "last_year" to one less than the current value of "year"

# TYPES
# Variables can hold more than just numbers
# there are four "primitive" types that python supports
age = 10  # integer, numeric whole number
weight_lbs = 16.2  # float, numeric floating point (decimal) number
name = "Bowie"  # string, non-numeric sequence of characters
is_dog = True  # boolean, true or false

# python also supports a few built-in data structures
# which hold multiple items. We will learn about each one
# in detail later on, but here they are so you're familiar
# list - ordered sequence of values (can mix values) that you can add to and remove from
grades = [10, 12, 4]
# tuple - ordered sequence of values that cannot be modified
coordinate = (8, 2)
# set - unordered collection of unique values
set = {"black", "blue", "orange"}
# dictionary - collection of key/value pairs
vehicle = {'make': 'Jeep', 'model': 'Wrangler', 'color': 'Army Green'}

# python is a dynamically typed language
# which means variables can switch types whenever you want
# and you do not have to specify the type when you assign a value
# this can get tricky though, so it is best practice to maintain a variable's type throughout its life
total_cost = 10  # as int
total_cost = 10.0  # as float
total_cost = "$10.00"  # as string

# you can also convert values from one type to another
# we will see more use cases for this as we go through the semester
age = int("21")  # turns string value of 21 to integer value

# FUNCTIONS
# functions are named entities that accept some input, run a set of statements, and return an output
# there are some functions built in to python
# and we can also create our own functions
# one example of a built-in function is the "print" function
# which takes an input of what to print and then writes it out to the terminal when the program is executed
print("The total cost is " + total_cost)
# here our input to the function is an expression that evaluates to a single string
# using what is called "string concatenation" (gluing together two strings)

# we can also get information from the user of our program
# by using the built-in "input" function
name = input("What is your name? ")
# this will print out the prompt given to the function to the terminal, wait for the user to type something and hit enter, and then save the value typed in to our variable
# the returned value from input() will ALWAYS be a string
# in this case, the call to the function input() is an expression that evaluates to whatever the user types in

# we can then use this value to print out a greeting to the user
print("Hello, " + name)

# now our program can be run multiple times with different input, and our code dynamically adjusts to it
