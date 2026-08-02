# Write a Python program to calculate the average of all elements in a list.

list =[]

i = 0 
while i < 5:
    num = int(input("Enter your number: "))
    list.append(num)
    i += 1

print(list)
# using sum method
sum_ = sum(list)

average = sum_/len(list)

print(f"The average of all elements in a list {average}")


# without using sum method

sun=0
for i in list:
    sun += i
    average = sun/len(list)


print(f"The average of all elements in a list {average}")