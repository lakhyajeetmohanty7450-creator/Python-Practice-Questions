# Write a Python program to create a Contact Book that allows users to add, 
# search, update, delete, and display contacts.
contact_book= {    "Rahul": 8589635896,
    "Amit": 9286478912,
    "Priya": 7886478912,
    "Sneha": 8886478912,
    "Rohan": 9586478912,
    "Anjali": 9864789120
    }

def add():
    a = input("Add your user name: ")
    b = input("user phone number: ")
    if len(b)== 10 and b.isdigit():
        contact_book[a]=int(b)
        print("Contact added successfully!")
    else:
        print("Invalid phone number")

def search():
    a = input("Enter your user name: ")
    if a in contact_book:
        print(f" {a}  < ---- >{contact_book[a]}")
    else:
        print("contact not found")

def modify():
    a = input("modify your user name: ")
    b = input("user phone number: ")
    if a in contact_book:
        if len(b)== 10 and b.isdigit():
            contact_book.update({a:int(b)})
            print("Contact modify successfully!")
        else:
            print("Not modify number")
    else:
        print("User not found")

def delet():
    a = input("Enter your delete user name: ")
    if a in contact_book:
        contact_book.pop(a)
    else:
        print("User not found")

def display_contacts():
    for keys , value in contact_book.items():
        print(f"|{keys}  |  {value}|")


while True:
    print("1 Add")
    print("2 Search")
    print("3 Update")
    print("4 Delete")
    print("5 Display contacts")
    print("6 Exit")

    chosse = int(input("Enter your choice "))
    if chosse == 1:
        add()
    elif chosse == 2:
        search()
    elif chosse ==3:
        modify()
    elif chosse == 4:
        delet()
    elif chosse == 5:
        display_contacts()
    elif chosse == 6:
        break

