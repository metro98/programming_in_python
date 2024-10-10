a = int(input("Enter the first number to print AP series of: "))
d = int(input("Enter the step size: "))
n = int(input("Enter the last number: "))

for i in range(a, n+1, 2):
    print(f"{i} ", end="")
