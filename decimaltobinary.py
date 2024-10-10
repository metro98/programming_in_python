
number = int(input("Enter a number to convert to binary: "))

binary = ''

while number > 0:
    remainder = number % 2
    number = number // 2
    binary = str(remainder) + binary

print(binary)


