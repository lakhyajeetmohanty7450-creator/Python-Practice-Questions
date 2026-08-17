                            # Write a Python program to generate a random password of a user-specified length.
import random
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
def passw(n):
    p = []
    i = 0
    while i<n:
        password = random.choice(characters)
        p.append(password)
        i +=1
    p1 = "".join(p)
    return(p1)

a = passw(n = int(input("Enter your password length: ")))
print(a,type(a))
