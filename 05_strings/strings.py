'''
Write a program that gets a sentence from the user 
and prints out that sentence with all occurrences of "o" 
turned into "oo" 
Example: I love coding -> I loove cooding
'''
# user_input = input("Enter a sentence: ")
# print(user_input.replace("o","oo"))


'''
Write a program that checks for curse words 
in a String of song lyrics. Your program should 
take a String and replace all occurrences of 
3 different profanities with "****". 
'''
# lyrics = "I see you riding round town with the girl I love and I'm like fuck you (oooo)"
# # method chaining
# censored = lyrics.replace("fuck","****").replace("girl","****").replace("rid","****").upper()
# print(censored)

'''
Write a program that takes dates written in the format 
MM-DD-YYYY and rewrites it more formally, in this format: 
DD Month, YYYY. 
Example: 01-01-2023 -> 01 January, 2023. 

Challenge: Write a program that converts the other way, 
from the formal date to the MM-DD-YYYY date.
'''
# date = "02-12-2023"
# month = date[:2]
# day = date[3:5]
# year = date[6:]

# if date[:2] == "01":
#     month = "January"
# elif month == "02":
#     month = "February"
# else: 
#     month = "Some Other Month"

# print(f"{day} {month}, {year}")

'''
Write a password verification program that gets the 
potential password from the user, and then verifies 
that the password meets the following criteria:
- password is greater than 8 characters long
- password includes one uppercase character
- password includes one of these special characters: !$@#&
Your program should tell the user if their password 
is valid or not.
'''
password = input("Password: ")
# you can set a variable to the result of an expression
has_length = len(password) > 8
has_uppercase = False
has_special = False

for character in password: 
    # go through each character
    # check if character is uppercase
    if character.isupper():
        has_uppercase = True
    # check if character is a special character
    if character in "!$@#&":
        has_special = True

if has_length and has_special and has_uppercase: 
    print("Your password is valid.")
else:
    print("Your password is too weak!")
