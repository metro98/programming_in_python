#Display multiplication table for a given number

number_multiplilcation = int(input("Enter the number you want the multiplicaton of: "))

for i in range(0, 11):
    print(f"{number_multiplilcation} * {i} = {number_multiplilcation * i}")

#Find the factorial of a given number

number_factorial = int(input("Enter the number you want the factorial of: "))


factorial = 1
for number in range(1, number_factorial + 1):
    factorial = factorial * number

print(factorial)