# Write a Python program to print the multiplication table of a number up to 20.

num = int(input("Enter your number: "))


i = 0 
while i <=10:
    print(f"multiplication table of {num} is {num}X{i} = {num*i}")
    i +=1