# Congraluations, you have got a job at Python Pizza! Your first job is to build an automatic pizza order program.
#
# Based on user's order, work out their final bill.
#
# Small pizza: 15$
# Medium pizza: 20$ 
# Large pizza: 25$
#
# Add pepperoni:
# 2 $ for small pizza
# 3 $ for medium or large pizza
#
# Add cheese: 1$ any size
#

print("Thank you for choosing Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M, or L").upper()
addPepperoni = input("Do you want pepperoni? Y or N").upper()
addCheese = input("Do you want extra cheese? Y o N").upper()

# Don't change the code above

total = 0
pepperoniCharge = 2

match size:
    case "S":
        total += 15
    case "M":
        total += 20
        pepperoniCharge = 3
    case "L":
        total += 25
        pepperoniCharge = 3
    case _:
        print("Wront size")
        exit(1)

if addPepperoni == "Y":
    total += pepperoniCharge

if addCheese == "Y":
    total += 1

print(f"The cost of the pizza is {total} $")
