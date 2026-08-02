# Write a Python program to determine whether a given year is a leap year or not.

year = int(input("Enter your year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("This is a leap year")
else:
    print("This is not a leap year")


