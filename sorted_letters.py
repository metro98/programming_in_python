#Enter a string
user_input = input("Enter a string")
sorted_input = sorted(user_input)
sorted_string = "".join(sorted_input)
print(f"The sorted input string is {sorted_string}")