age = input()
# Don't change the code above
# Write your code below

if not age.isdigit():
    print(f"input [{age}] is not a number")
    exit(1)

years = 90 - int(age)
weeks = years * 52

print(f"You will die in {weeks} weeks")
