# Write a Python program to determine whether a given string is a palindrome.

str = input("Enter your string: ")

list = []

for i in str:
    list.append(i)

list.reverse()
str2= "".join(list)
print(str2)


if str == str2:
    print("palindrome")
else:
    print("not palindrome")