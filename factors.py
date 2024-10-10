n = int(input("Enter the number you want the factor of: "))
for i in range(1, n + 1):
    if n % i == 0:
        print(i)


