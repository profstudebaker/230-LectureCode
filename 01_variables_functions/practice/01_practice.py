"""
PROBLEM 1
Write a program that gets 2 numbers from a user and then prints out their sum and their product.
"""
# use the input() function to get values from user
# INPUT IS ALWAYS A STRING so we must type-cast it to an int
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

# to print both strings and numeric types, we can use commas
print("You entered ", num1, "and", num2)
# or we can type-cast the numeric type to a string
print("Sum: " + str(num1 + num2))
print("Product: " + str(num1 * num2))

