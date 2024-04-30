inputs = "-75.6,102.75,0.0087,125145.21"

values = inputs.split(",")

maxValue = 0

for value in values:
    v = float(value)
    if v > maxValue:
        maxValue = v

print(f"The maximum value is {maxValue}")
