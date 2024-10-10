import random


print("Let's play a game. You guess the number I choose")

guess_number = random.randint(1,10)
print(guess_number)


count = 0
while count < 3:
    number = int(input("Enter your guess and you get 3 try: "))
    if number == guess_number:
        print("You found it")
        break
    elif number > guess_number:
        print("Too high")
        count = count + 1
    elif number < guess_number:
        print("Too low ")
        count = count + 1
    
    if count == 3:
        print("You loose")


