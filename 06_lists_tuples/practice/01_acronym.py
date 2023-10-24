'''
Write a program that gets a name of an organization 
or term from the user and then prints out the 
acronym of that organization/term, using the first 
letter of each word. 
For example: "Student Government Association" -> "SGA"
'''
org = input("Enter an organization: ")
# org = "student Government association"
# by default, split cuts the string at each space
words = org.split() # ['Student', 'Government', 'Association']
acronym = "" # start with an empty string
for word in words: 
    first_letter = word[0].upper()
    acronym += first_letter # add on to acronym
print(f"Your acronym is: {acronym}")




'''
Challenge: Adapt your program so that words like "the" 
"of" and "a" are not included in the acronym. 
For example: "Federal Bureau of Investigation" -> "FBI"  
'''
org = input("Enter an organization: ")
words_to_skip = ("of", "the", "a")
org = "federal bureau OF investigation"
# by default, split cuts the string at each space
words = org.split()
acronym = "" # start with an empty string
for word in words: 
    if word.lower() not in words_to_skip:
        first_letter = word[0].upper()
        acronym += first_letter # add on to acronym
print(f"Your acronym is: {acronym}")



'''
Challenge: Modify your solution to use list comprehension.
'''
words_to_skip = ("of", "the", "a")
org = "federal bureau OF investigation"
acronym = "".join([word[0].upper() for word in org.split() if word.lower() not in words_to_skip])
print(acronym)