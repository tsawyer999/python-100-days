# Enter your height in meters
height = input()

# Enter your weight in kilograms
weight = input()

############################################
# Your code below this line
############################################

convertedHeight = float(height)
convertedWeight = float(weight)

bmi = round(convertedWeight / convertedHeight ** 2, 2)

if bmi < 18.5:
    objectName = "feather"
elif bmi < 25:
    objectName = "beer keg"
elif bmi < 30:
    objectName = "kangaroo"
elif bmi < 35:
    objectName = "bathtub"
else:
    objectName = "cubic meter of snow"

print(f"Your BMI is {bmi}, you weight is like a {objectName}.")
