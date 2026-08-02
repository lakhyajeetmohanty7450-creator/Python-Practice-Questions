# Write a Python program to calculate the Greatest Common Divisor (GCD) of two numbers.
import math

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

GCD = math.gcd(num1,num2)
print(f"The Greatest Common Divisor of {num1} and {num2} is: {GCD}")


#without using math module

num1 = int(input("Enter your number: "))
num2 = int(input("Enter your number: "))

if num2 > num1:
    min = num1
else:
    min = num2

for i in range(1,min+1):
    if num1 % i == 0 and num2 % i == 0:
        hcf = i

print ("your HCF is: " , hcf)
