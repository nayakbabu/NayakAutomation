#this is a program for a loop that keeps asking for a password until the user enters the correct one

correct_password = "python123"

while True:
    password = input("Enter your password: ")

    if password == correct_password:
        print("Access granted.")
        break
    print("Wrong password. Try again..")