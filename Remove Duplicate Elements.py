# Write a Python program to remove duplicate elements from a list.

list_ =[]

i =0
while i < 5:
    num = int(input("Enter your element: "))
    list_.append(num)
    i += 1

print(list_)
a=set(list_)

print(f"The list after removing duplicate elements {list(a)}")

# after removing duplicate elements from a list using for loop

list_ =[]
list_2 = []

i =0
while i < 5:
    num = int(input("Enter your element: "))
    list_.append(num)
    i += 1

for i in list_:
    if i not in list_2:
        list_2.append(i)

print(f"The list after removing duplicate elements {list_2}")