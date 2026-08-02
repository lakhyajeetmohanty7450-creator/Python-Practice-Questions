# Write a Python program to count the number of digits in a given integer.
num1 = int(input("Enter your number: "))
num2 = str(num1)
list = []
for i in num2:
    list.append(i)



print(f"The number of digits in a given integer {len(list)}")
