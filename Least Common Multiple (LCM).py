# Write a Python program to calculate the Least Common Multiple (LCM) of two numbers.
import math

num1 = int(input("Enter the first number: "))
mum2 = int(input("Enter the second number: "))

LCD = math.lcm(num1,mum2)
print(f"The Least Common Multiple of {num1} and {mum2} is: {LCD}")

#without using math module


num1 = int(input("Enter your number: "))
num2 = int(input("Enter your number: "))

max_ = max(num1,num2)

while (True):
    if (max_%num1==0 and max_%num2==0):
        
        break
    max_ = max_ +1

print(f"LCM IS {max_}")



        