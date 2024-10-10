
#Total numbers user can enter
number_of_numbers = int(input("Enter the number of digits for the sum: "))
count = 0
total = 0
highest = 0
while count < number_of_numbers:
    numbers = int(input("Enter the number: "))
    total = total + numbers
    if highest < numbers:
        highest = numbers
    count += 1

print(f"The sum of the numbers is: {total}")

#maximum number
print(f"The highest number is: {highest}")


