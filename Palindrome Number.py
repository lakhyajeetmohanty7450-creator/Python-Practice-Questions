# Write a Python program to determine whether a given number is a palindrome.
num1 = int(input("Enter your number: "))

str = str(num1)
list = []

for i in str:
    list.append(i)

list.reverse()
str2= "".join(list)


num2 = int(str2)
if num1==num2:
    print("palindrome")
else:
    print("not palindrome")
   