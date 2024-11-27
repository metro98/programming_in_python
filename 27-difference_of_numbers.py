def difference(a, b):
    diff = a - b
    diff = abs(diff)

    if diff <= 5:
        return True

    else:
        return False

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

print(difference(first_number, second_number))