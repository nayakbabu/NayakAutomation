#This program is a number guessing playground

secret_number = 7

guess = int(input("Guess a number from 1 to 10: "))

if guess == secret_number:
    print("Correct --Nice work!")
elif guess < secret_number:
    print("Too low.")
else:
    print("Too High.")