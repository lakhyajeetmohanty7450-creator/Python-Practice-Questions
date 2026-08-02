# Write a Python program to find the second largest element in a list.


list = []
i = 0

while i<5:
    num = int(input("Enter your element: "))
    list.append(num)
    i += 1

print(list)

max =list[0]

for i in list:
    if i >max:
        max = i

second_max = list[0]


for i in list:
    if i > second_max and i != max:
        second_max = i
        

print(f"the second largest element in a list {second_max}")


    