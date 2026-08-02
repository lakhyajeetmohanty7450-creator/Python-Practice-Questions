# Write a Python program that repeatedly asks the user to enter a number until the correct number is entered.

num= int(input("Enter your number: "))

a = 7

while(True):
    if num == 7:
        print("You choose correct number")
        break
    num = int(input("Enter your number again: "))
