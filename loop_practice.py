

def even_number(a, b):
    even = []
    for i in range(a, b+1):
        if i % 2 ==0:
            even.append(i)
    
    return even
        

number = even_number(1, 20)
for i in number:
    print(i, end = " ")

def factorial(n):
    fact = 1
    while n >= 1:
        fact = n * fact
        n = n -1
    return fact

print(factorial(5))

def reverse(word):
    total_length = len(word)
    reverse = [None] * total_length
    for i in range(total_length):
        reverse[total_length - 1 - i ] = word[i]
    return "".join(reverse)


print(reverse("hello"))

