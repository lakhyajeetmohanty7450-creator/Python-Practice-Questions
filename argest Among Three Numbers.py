# Write a Python program to accept three numbers from the user and display the largest number.
list = []
i = 0
while i < 3:
    a=int(input("Enter your number: "))
    list.append(a)
    i += 1

max = max(list)
print(f"Largesr number is : {max}")