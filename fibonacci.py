n = int(input("Enter the number of series: "))
first = 0
second = 1
print(first, end=" ")
print(second, end=" ")
for i in range(0, n):
    sum = first + second
    print(sum, end = " ")
    first = second
    second = sum
    
