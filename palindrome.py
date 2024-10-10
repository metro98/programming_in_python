

#Enter a number
number = int(input("Enter a number of your choice: "))

#Find the sum of digits in a number
count = 0
sum = 0
reverse_number = 0
temp = number

while temp > 0:
    remainder = temp % 10
    sum = sum + remainder
    reverse_number = reverse_number * 10 + remainder
    temp = temp // 10

print(f"The sum of the given number is : {sum}")

#Reversing a number
print(f"The reverse number is: {reverse_number}")

#Check for palindrome
if number == reverse_number:
    print("The number is a palindrome")
