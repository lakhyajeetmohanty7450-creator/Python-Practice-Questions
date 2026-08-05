# Write a Python program to determine whether a password is strong based on the following conditions:

# Minimum length of 8 characters
# At least one uppercase letter
# At least one lowercase letter
# At least one digit

passw = input("Enter your password: ")

has_upper = False
has_lower = False
has_digit = False

for i in passw:
    if i.isupper():
        has_upper = True
    elif i.islower():
        has_lower = True
    elif i.isdigit():
        has_digit = True

if len(passw) > 8 and has_upper and has_lower and has_digit:
    print("Strong password")
elif len(passw) > 8 and has_upper and has_lower :
    print("password needs is atleast one number")
elif len(passw) > 8 and has_digit and has_upper:
    print("password needs is atleast one lower case")
elif len(passw) > 8 and has_digit and has_lower:
    print("password needs is atleast one upper case ")
elif has_upper and has_lower and has_digit:
    print("password length must be 8")
else:
    print("password is very weak")







  

    
    