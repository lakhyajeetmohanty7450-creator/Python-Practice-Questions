# Write a Python program to check whether an email address
# entered by the user is valid by verifying that it contains '@' and '.' characters

email = input("Enter your email: ")




if email.count("@") == 1 in email and "." in email:
    print("Valid")
else:
    print("Not Valid")
    
        
    