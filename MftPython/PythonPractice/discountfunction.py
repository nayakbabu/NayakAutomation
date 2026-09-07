#This is anotehr function practice program logic is calculate discount 

def calculate_discount(price, discount_percent):
    discount_amount = price * discount_percent /100
    final_price = price - discount_amount
    return final_price

new_price = calculate_discount(100, 20)
print("Final price:", new_price )