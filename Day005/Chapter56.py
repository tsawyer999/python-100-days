# Implement the FizzBuzz challenge

for i in range(1, 101):
    isDivisibleBy3 = False
    if i % 3 == 0:
        isDivisibleBy3 = True

    isDivisibleBy5 = False
    if i % 5 == 0:
        isDivisibleBy5 = True

    if not isDivisibleBy3 and not isDivisibleBy5:
        print(i, end='')

    if isDivisibleBy3:
        print("Fizz", end='')

    if isDivisibleBy5:
        print("Buzz", end='')

    print("")
