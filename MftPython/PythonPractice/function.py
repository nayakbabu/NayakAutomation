# In this class we will learn function
# def should be the starting means "define a function"
#function should have a name

def greet(name):
    print("Hello, " + name + "!")
greet("Satya")
greet("Sam")

#This is another function for your practice

def introduce(name, city):
    print("My name is " + name + ".")
    print("I live in " + city + ".")
introduce("Nayak", "Sofia")

#practice another function students 

def employees(name ,age):
    print("Employee name is " + name )
    print("Employee age is " + age )
employees("Satya", "35")
employees("Smita", "32")


#write another function

def company (name, location, function):
    print("Company name is " + name )
    print("This is located in " + location)
    print("The main function is " + function)

company("Axway", "Paris", "Product develpement")
company("IBM", "usa", "Consulting")
company("Google", "usa", "Search engine")

#now improve the above function with some industry standard function writing 

def company(name, location, function):
    return f"Company name is {name}, it is located in {location}, main function is {function}"
print(company("Axway", "paris", "product developement"))
print(company("IBM", "usa", "Consulting"))
print(company("Google", "usa", "Search engine"))

#practice another function for students lab

def greet_user(name, role="Enginner"):
    return f"Hello {name}, welcome onboard in {role}"
print(greet_user("Nayak"))
print(greet_user("Nayak", "devops enginner"))

#practice some more functions 

def addition(x, y):
    return x + y
print(addition(10, 5))

#find maximum of two numbers via a function

def maximum(a, b):
    if a >b:
        return a
    else:
        return b
print(maximum(12 , 6))
