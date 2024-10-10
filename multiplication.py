
continue_play = True
while continue_play:
    number = int(input("Enter the number you want the multiplication of: "))

    count = 1

    while count <= 10:
        result = number * count
        print(f"{number} * {count} = {result}")
        count = count + 1
    
    answer = input("Do you want to try another number(y/n): ")
    if answer == "n":
        continue_play = False
    else:
        continue_play = True
