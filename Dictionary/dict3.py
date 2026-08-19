# Construct a dictionary containing four product names and their
# prices. Prompt the user to enter a product name. Use the in
# keyword to check if it exists; if so, display its price. Otherwise,
# inform the user "Product not found".

products = {
    "Laptop": 50000,
    "Phone": 20000,
    "Headphones": 3000,
    "Keyboard": 1500
}

a = input("Enter you product you want: ")

if a in products:
    print(f"Your product name is {a} and price is {products[a]}")
else:
    print("Product not found")