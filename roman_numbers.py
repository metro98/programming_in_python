roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

roman_input = input("Enter the roman number: ")

decimal_number = 0
i = 0
while i < (len(roman_input)):
    if i+1 < (len(roman_input)) and roman[roman_input[i]] < roman[roman_input[i + 1]]:
        decimal_number = decimal_number + roman[roman_input[i + 1]] - roman[roman_input[i]]
        i = i + 2
    

    else:
        decimal_number = decimal_number + roman[roman_input[i]]
        i = i + 1

print(decimal_number)





