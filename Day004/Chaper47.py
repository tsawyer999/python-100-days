line1 = [" ", " ", " "]
line2 = [" ", " ", " "]
line3 = [" ", " ", " "]

theMap = [line1, line2, line3]

print("Hiding your treasure! X marks the spot.")

position = input("Where do you want to put the treasure?\n")

# Don't change the code above
# Write your code below this row

horizontalIndex = ord(position[0].lower()) - 97
verticalIndex = int(position[1]) - 1

theMap[horizontalIndex][verticalIndex] = "X"

print("\n")
print(f"{line1}\n{line2}\n{line3}")
print("\n")
print(f"The treasure is located at {horizontalIndex}-{verticalIndex}")
print("\n")
