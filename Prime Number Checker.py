# Write a Python program to check whether a given number is prime or not.
num = int(input("Enter your number: "))

if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("This is not a prime number")
            break
    else:
        print("This is a prime number")
else:
    print("This is not a prime number")


