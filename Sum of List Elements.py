# Write a Python program to calculate the sum of all elements in a list.

list = []

i = 0
while i<6:
    num = int(input("Enter your number: "))
    list.append(num)
    i += 1

print(list)
print(f"The sum of all elements in a list {sum(list)}")


# without using sum method

list = []

i = 0
while i<6:
    num = int(input("Enter your number: "))
    list.append(num)
    i += 1

sum = 0


for i in list:
    sum += i

print(f"The sum of all elements in a list {sum}")
