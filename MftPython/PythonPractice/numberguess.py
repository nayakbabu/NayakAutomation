#This program is a number guessing playground

secret_number = 7
guess_left = 3
won = False
while guess_left > 0:
    guess = int(input("Guess a number from 1 to 10: "))
    if guess == secret_number:
        print("Correct — you win!")
        won = True
        break
    elif guess < secret_number:
        print("Too Low.")
    else:
        print("Too High.")
    guess_left = guess_left -1
    print("Guesses left: ",guess_left)
if won == False:
    print("You ran out of guesses. The number was", secret_number)

