# Write a Python program to count the total number of even digits and odd digits in a given number.
# 248135
# Even digits = 3
# Odd digits = 3

num1 = int(input("Enter your number: "))
even = 0
odd = 0
str = str(num1)
list=[]

for i in str:
    list.append(i)

for i in list:
    int_ = int(i)
    if int_ % 2 == 0 :
        even += 1
    else:
        odd += 1

print(f"Even digits = {even}")
print(f"Odd digits = {odd}")


