# Write a Python program to calculate the sum of the first N natural numbers.

num = int(input("Enter your number: "))
list = []
i = 0
while i <= num:
    list.append(i)
    i +=1

sum = sum(list)
print(f"The sum of the first N natural numbers {sum}")