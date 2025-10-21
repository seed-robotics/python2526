import random

print("Hello! You must guess a number between 1 and 100\n")
while True:
    tries = 0
    randNum = random.randint(1, 100)
    while tries < 6:
        while True:
            try:
                uNum = int(input("Type your number (1-100): "))
                if 1 <= uNum <= 100:
                    break
                else:
                    print("Number must be between 1 and 100.")
            except ValueError:
                print("Please enter a valid integer!")

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
    
    play_again = input("Press Enter to play again or type QUIT to stop: ").upper()
    if play_again == "QUIT":
        print("Thanks for playing!")
        break
