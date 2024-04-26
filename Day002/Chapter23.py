height = input()
weight = input()

############################################
# Your code below this line
############################################

convertedHeight = float(height)
convertedWeight = float(weight)

bmi = convertedWeight / convertedHeight ** 2

print(f"Your BMI is {round(bmi, 2)}")
