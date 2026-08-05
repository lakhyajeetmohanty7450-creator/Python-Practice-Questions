# Write a Python program to find the student who has scored the highest marks from a dictionary.
list1=[]
num = int(input("Enter your total class student number: "))
i = 0
while i < num:
    name = input("Enter Name: ")
    roll = input("Enter Roll: ")
    mark = input("Enter total mark: ")

    dict1={"Name":name , "Roll Number":roll , "Mark":mark}

    list1.append(dict1)

    i +=1

marks = list1[0]

for a in list1:
    if a["Mark"] > marks["Mark"]:
        marks = a

print("\nStudent with Highest Marks")
print(marks["Name"])

#  ///////////////////////////////////////////////////////////////////////////////////////////

students = [
    {"Name":"A","Mark":100},
    {"Name":"B","Mark":190},
    {"Name":"C","Mark":180}
]
topper = students[0]

for a in students:
    if a["Mark"] > topper["Mark"]:
        topper = a

print(f"Topper is {topper['Name']}")
print(f"Marks: {topper['Mark']}")