# Write a Python program to merge two lists into a single list.

list=[]
list2=[]
i = 0
while i < 5:
    num = int(input("Enter a number for the first list: "))
    list.append(num)
    i +=1

j = 0
while j < 6:
    num = int(input("Enter a number for the second list: "))
    list2.append(num)
    j +=1

    

print(list)
print(list2)

c = list + list2

print("Merged list is: ", c)
