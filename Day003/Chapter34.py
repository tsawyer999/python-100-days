# Which year do you want to check?
year = int(input())

# Don't change the code above

isLeapYear = False

if year % 4 == 0:
    if year % 100 != 0:
        isLeapYear = True
    elif year % 400 == 0:
        isLeapYear = True

if isLeapYear:
    print(f"Year {year} is a leap year")
else:
    print(f"Year {year} is not a leap year")
