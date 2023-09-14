# import every function from our other file
# when we have code in a __main__ module
# it does not get run on import, only on execution
from function_basics import * 

print(motherlode(5)) # shoulde be 500

print(generate_greeting("Good Sir")) # should be Howdy, Good Sir!

print(generate_greeting("Good Sir", "Good Evening")) # should be Good Evening, Good Sir!