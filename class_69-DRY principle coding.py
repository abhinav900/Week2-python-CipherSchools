# Modify number guessing game
import random
wining_number = random.randint(1,100)
guess = 1
game_over= False

while True:
    number = int(input("Guess a number between 1 and 100: "))

    if number == wining_number:
        print(f"You win and you guessed this number in {guess} times ")
        break
    else:
        if number < wining_number:
            print("Too Low")

        else:
            print("Too High")

        guess += 1
        continue


# DRY --> Do not repeat yourself
