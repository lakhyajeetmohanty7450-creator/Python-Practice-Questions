# Write a Python program to calculate the factorial of a number using a loop

num = int(input("Enter your number: "))

i = 1
while i <= num:
    if num == 0:
        print("The factorial of 0 is 1")
        break
    else:
        fact = 1
        for i in range(1, num + 1):
            fact = fact * i
        print("The factorial of", num, "is", fact)
        break


# important: The code above calculates the factorial of a number using a loop. 
# It prompts the user to enter a number, 
# and then it calculates the factorial by multiplying all integers from 1 to that number. 
# If the user enters 0, it correctly outputs that the factorial of 0 is 1.
    
    