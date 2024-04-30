target = int(input("Enter a number between 0 and 1000"))
# Do not change the code above

if target < 0:
    print("Number must be more than 0")

if target > 1000:
    print("Number must be less or equal than 1000")

result = 0
for x in range(2, target+1):
    if x % 2 == 0:
        result += x

print(f"The sum of all even number between 2 and {target} is {result}.")
