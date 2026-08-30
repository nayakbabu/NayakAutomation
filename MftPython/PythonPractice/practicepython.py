#This is a comment python will ignore this line, its just  a note for other human's or developers
# This program is to know how print works
print("Hello Infra world|")
print(34)
print(3.14)

#Variables and data types program practice

name = "Nayak"   #string datatype
age = 34         # integer datatype
height = 5.7     # float datatype
is_practicing = True #boolean datatype
print(name, age, height, is_practicing, sep=", ")
print(type(name))

#Another data type practice

x = 10
y = "10"

print(x + 10)
print(y + "10")

#basic operator 

a = 10
b = 3

print(a + b)   #addition
print(a - b)   #abstraction
print(a * b)   #Multiplication 
print(a / b)   #division
print(a // b)  #floor division
print(a % b)   #modules
print(a ** b)  #exponent

# next practice will be input from the user

user_name = input("What's your name? ")
print("Welcome onboard, " + user_name + "!")

# age = input("Enter your age: ") #This will throw error 
# print(age + 1)

age = int(input("Enter your age: "))
print(age + 1)

#Next practice will be conditional statements 

score = int(input("Enter your test score: "))

if score >= 90:
    print("Grade: A")
elif score >= 75:
    print("Grade: B")
elif score >= 50:
    print("Grade: C")
else:
    print("Grade: F")


# another program with conditional statements 

temperature = 35
is_raining = False

if temperature > 30 and not is_raining:
    print("Great day for outdoor activites including testing")


# this practice is for loop

for i in range(5):
    print("Iteration:", i)

servers = ["web01", "web02", "db01"]
for server in servers:
    print("Checking server:", server)

#next practice is for while loop

count = 0
while count < 5:
    print("Count is", count)
    count += 1


#next practice will be lists and dictionaries 

servers = ["Web01", "Web02", "db01"]
print(servers[0])
servers.append("Web03")
print(servers)
print(len(servers))

#next practice will be for dictionary 

server_status = {
    "web01": "running",
    "web02": "stopped",
    "db01": "running"
}

print(server_status["web01"])   #running
for server, status in server_status.items():
    print(server, "is", status)

# finally in this program we will write a function

def check_server(name, status):
    if status == "running":
        print(name, "is healthy")
    else:
        print(name, "needs immediate attention")

check_server("web01", "running")
check_server("web02", "stopped")