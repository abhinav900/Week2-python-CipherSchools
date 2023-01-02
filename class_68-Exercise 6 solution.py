# Modify number guessing game

wining_number=41
guess = 1
number=int(input("Guess a number between 1 and 100: "))
game_over= False

while not game_over:
    if number == wining_number:
        print(f"You win and you guessed this number in {guess} times ")
        game_over=True
    else:
        if number < wining_number:
            print("Too Low")
            guess+=1
            number = int(input("Guess again: "))
        else:
            print("Too High")
            guess+=1
            number = int(input("Guess again: "))

