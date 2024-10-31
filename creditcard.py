card = input("Enter the card number: ")

dots = "*" * 4
last_number = card.rsplit(" ",1)
last = last_number[1]


display = dots + " " + dots + " " + dots + " " + last
print(display)