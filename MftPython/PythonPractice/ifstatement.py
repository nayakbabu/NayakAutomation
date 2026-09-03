age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult in India. ")
else:
    print("You are an underage minor of India. ")

score = int(input("Enter your score: "))

if score >= 90:
    print("You are an excellent student")
elif score >= 60:
    print("You are an above average student")
elif score >= 40:
    print("You are an average student")
else:
    print("You are a worst student")

for number in range(1, 6):
    print(number)

for age in range(24, 30):
    print(age)