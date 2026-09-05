# We will learn today function with a game type use case

def play_guessing_game():
    secret_number = 7
    guesses_left = 3
    won = False

    print("Guess the secret number from 1 to 10.")
    print("You have 3 guessses")

    while guesses_left > 0:
        guess = int(input("Your guess: "))

        if guess == secret_number:
            print("Correct — you win!")
            won = True
            break
        elif guess < secret_number:
            print("Too low.")
        else:
            print("Too High.")
        guesses_left = guesses_left - 1
        print("Guesses left:", guesses_left)
    if won == False:
        print("You ran out of guesses.")
        print("The secret number was", secret_number)
play_guessing_game()