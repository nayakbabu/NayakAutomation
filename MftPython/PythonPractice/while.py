count = 1
while count <= 5:
    print(count)
    count = count + 1



foods = ["pizza", "sushi", "Biriyani"]

for food in foods:
    print("I like", food)

fruits = ["Banana", "Apple", "Orange"]

for fruit in fruits:
    print("I like", fruit)


number = int(input("Enter a number: "))

for multiplier in range(1, 11):
    print(number, "x", multiplier, "=", number * multiplier)