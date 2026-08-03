# Write a Python program to count the positive and negative numbers in a list.

list =[]
positive  = 0
negative = 0


i = 0
while i<5:
    num = int(input("Enter your element: "))
    list.append(num)
    i += 1

for i in list:
    if i >0 :
        positive +=1
    else:
        negative +=1

print(list)

print(f"The count of positive numbers in a list {positive}")
print(f"The count of negative numbers in a list {negative}")
