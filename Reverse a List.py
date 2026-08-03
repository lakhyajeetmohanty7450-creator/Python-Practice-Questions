# Write a Python program to reverse the elements of a list without using the reverse() method.

list = []
list2 = []

i = 0
while i<5:
    num = int(input("Enter your number: "))
    list.append(num)
    i += 1

print(list)

print(f"The reverse of the list is {list[::-1]}")

