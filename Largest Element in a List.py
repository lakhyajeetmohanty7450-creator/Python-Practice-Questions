# Write a Python program to find the largest element in a list.

list =[]

i = 0

while i < 5:
    num=int(input("Enter your element: "))
    list.append(num)
    i +=1
print(list)

# use max method

print(f"The largest element in a list {max(list)}")

# without use max method


max_ = list[0]

for i in list:
    if i > max_:
        max_ == i

print(f"The largest element in a list {max_}")

