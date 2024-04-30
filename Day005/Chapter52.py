inputs = "1.692,1.75,0.87,1.21"

heights = inputs.split(",")

total = 0

for height in heights:
    total += float(height)

average = total / len(heights)

print(f"The average height is {average:.1f}")
