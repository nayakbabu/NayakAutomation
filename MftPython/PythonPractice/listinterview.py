# This program separate even and odd numbers 

list = [1,2,3,4,5,6,7,8,9]
even = [x for x in list if x % 2 == 0]
odd = [x for x in list if x % 2 != 0]

print("Even:", even)
print("Odd:", odd)


#another list practice

list1 = [11,12,13,14,15,16,17,18,19,20]

odd1 = [x for x in list1 if x % 2 != 0]
even1 = [x for x in list1 if x % 2 == 0]
print("Odd:", odd1)
print("even:", even1)