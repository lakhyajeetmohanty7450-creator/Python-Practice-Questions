# Merge Dictionaries
student1 = {
    "Name": "Luna",
    "Roll": 21
}

student2 = {
    "Mark": 95,
    "Grade": "A"
}


student1.update(student2)

print(student1)


book1 = {
    "Title": "Python",
    "Author": "Guido"
}

book2 = {
    "Price": 599,
    "Pages": 450
}


book1.update(book2)
print(book1)


dict1 = {
    "A": 10,
    "B": 20,
    "C": 30
}

dict2 = {
    "D": 40,
    "E": 50,
    "F": 60
}


dict1.update(dict2)

print(dict1)