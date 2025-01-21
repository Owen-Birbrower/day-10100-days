adding = 4 + 3
print(adding)

subtraction = 8 - 9
print(subtraction)

multiplication = 4 * 32
print(multiplication)

division = 50 / 5
print(division)

# 5 to the power of 2
squared = 5**2
print(squared)

# remainder of a division
modulo = 15 % 4
print(modulo)

# whole number division
divisor = 15 // 2
print(divisor)


print("-- Bill Calculator --")
party = int(input("How many people are in your dinner party? "))
total = float(input("What is the total bill? "))
tip = int(input("What percentage tip would you like to leave? "))
yourSubTotal = total / party
yourTip = yourSubTotal * (tip / 100)
yourTotal = round((yourSubTotal + yourTip), 2)
print("You owe: ", yourTotal)

