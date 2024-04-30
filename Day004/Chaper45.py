import random

names_string = "Angela, Ben, Jenny   ,    Michael,    Chloe   "

# Don't change the code above

names = []

for value in names_string.split(","):
    names.append(value.strip())

randomIndex = random.randint(0, len(names)-1)
randomName = names[randomIndex]

print(f"{randomName} is going to buy the meal today!")
