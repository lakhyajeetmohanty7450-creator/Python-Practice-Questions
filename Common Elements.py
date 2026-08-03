# Write a Python program to find all common elements between two lists.

list1 = []
list2 =[]

i = 0
while i < 3:
    num = int(input("Enter a number for the first list: "))
    list1.append(num)
    i += 1

j = 0  
while j < 4:
    num = int(input("Enter a number for the second list: "))
    list2.append(num)
    j += 1

list3 = []

for a in list1:
    for b in list2:
        if a==b:
            list3.append(a)

print(list1)
print(list2)
print("Common elements are: ", list3)