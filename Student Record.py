# Write a Python program to store the Name,
# Roll Number, and Marks of five students using dictionaries and display the record
list1=[]

i = 0
while i < 2:
    name = input("Enter Name: ")
    roll = input("Enter Roll: ")
    mark = input("Enter total mark: ")
    dict={"Name":name , "Roll Number":roll , "Mark":mark}
    list1.append(dict)
    i +=1

print(list1)

