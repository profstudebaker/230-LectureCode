nums = []
with open("numbers.txt", "r") as f:
    for line in f:
        num = int(line)
        nums.append(num)

print(min(nums))

guest_list = []
name = input("Enter a name to invite (enter quit to quit): ")
while name != "quit":
    guest_list.append(name)
    name = input("Enter a name to invite (enter quit to quit): ")

print("Thanks! Saving your guest list...")
with open("guests.txt", "w") as out:
  for name in guest_list:
    out.write(name + "\n") 


teams = {}
with open("data.csv","r") as data:
  counter = 0
  for line in data:
    if counter != 0:
      # skip the header row
      # use the comma to get data
      data = line.strip('\n').split(",") 
      teams[data[0]] = {
        "wins": int(data[1]),
        "losses": int(data[2])
      }
    counter+=1

print(teams)
print(f"France has won {teams['France']['wins']} games.")
