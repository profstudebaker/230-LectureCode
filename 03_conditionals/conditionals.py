"""
Print out a menu to the user 
asking them if they want an inspirational quote, 
song lyric, or affirmation. Based on their choice, 
print out the appropriate response.
"""
print("""
-- Menu --
1 - Quote
2 - Song
3 - Affirmation
""")
choice = input("Select an option (1/2/3):")
if choice == "1":
    print("Quote")