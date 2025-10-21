import random

print("Hello! You must guess a number between 1 and 100\n")
while True:
    tries = 0
    randNum = random.randint(1, 100)
    while tries < 6:
        uNum = int(input("Type your number (1-100): "))
        tries += 1
        if uNum < randNum:
            print("Your guess is lower!\n")
        elif uNum > randNum:
            print("Your guess is higher!\n")
        else:
            print(f"Right on! Your guess took", tries, "tries\n")
            break
    else:
        print(f"Sorry you lost. The number was {randNum}\n")