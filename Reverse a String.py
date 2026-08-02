# Write a Python program to reverse a string entered by the user.

str = input("Enter your string: ")

list = []

for i in str:
    list.append(i)

list.reverse()
str2= "".join(list)
print(str2)


