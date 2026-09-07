#This is anotehr function practice program logic is calculate discount 

def calculate_discount(price, discount_percent):
    discount_amount = price * discount_percent /100
    final_price = price - discount_amount
    return final_price

new_price = calculate_discount(100, 20)
print("Final price:", new_price )

# This is another program practice with logic area of rectangle 

def calculate_area(length, width):
    rectangle_area = length * width
    return rectangle_area


area = calculate_area(5, 4)
print(area)