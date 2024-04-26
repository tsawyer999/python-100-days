
elements = "126a54"
total = 0

for element in elements:
    if "0" <= element <= "9":
        total += int(element)

print(f"The sum is {total}")

