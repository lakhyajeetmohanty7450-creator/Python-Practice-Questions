# # # Write a Python program to create a Shopping Cart and Billing System.

products = {
    "Apple": 50,
    "Banana": 30,
    "Milk": 60,
    "Bread": 40,
    "Eggs": 70,
    "Rice": 80,
    "Sugar": 45,
    "Biscuits": 25
}

shopping_cart={}
quantity = {}
total_ ={}

def product():
    for number ,(keys,value) in enumerate(products.items(),start=1):
        print(f" {number} . {keys}   {value}")
    print("9.Chekout")

def select():

    if p in products:
        shopping_cart.update({p:products[p]})
        quantity.update({p:q})
        total = quantity[p]*shopping_cart[p]
        total_.update({p:total})
        print(f"{p} added successfully!")
    else:
        print("product not found")

def bill():
    total_bill = sum(total_.values())
    print("========================BILL =====================")
    for name,price in shopping_cart.items():
        print(f"{name} | Quantity: {quantity[name]} | price {price} | Total {total_[name]}")
    print("-"*50)
    print(f"Total Bill {total_bill }")

product()

while True:     
    num ={}
    for number ,(keys,value) in enumerate(products.items(),start=1):
        num.update({number:keys})
    p = int(input("Enter your option: "))
    if p in num:
        p = num[p]         
        q = int(input("Enter quantity:"))
        select()
    elif p == 9:
        break
bill()