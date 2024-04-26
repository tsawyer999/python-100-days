# If the bill was 150.00$, split between 5 peoples, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.60$
# Round the result to 2 decimal places = 33.60$

print("Welcome to the tip calculator!")
inputBill = input("What was the total bill?")
inputTipPercentage = input("How much tip would you like to give?")
inputPersonCount = input("How many people to split the bill?")

bill = float(inputBill)
tip = int(inputTipPercentage) / 100
personCount = int(inputPersonCount)

billPerPerson = bill / personCount
amount = billPerPerson * (1 + tip)

print(f"Each person should pay {amount:.2f} $")
