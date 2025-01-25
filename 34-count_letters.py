user_input = input("Enter a string: ")

def count_number(phrase):
    upper_case = 0
    lower_case = 0
    for i in phrase:
        if i.islower():
            lower_case += 1
        elif i.isupper():
            upper_case += 1

    return upper_case, lower_case

print(count_number(user_input))

