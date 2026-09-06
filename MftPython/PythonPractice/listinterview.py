# This program separate even and odd numbers 

list = [1,2,3,4,5,6,7,8,9]
even = [x for x in list if x % 2 == 0]
odd = [x for x in list if x % 2 != 0]

print("Even:", even)
print("Odd:", odd)