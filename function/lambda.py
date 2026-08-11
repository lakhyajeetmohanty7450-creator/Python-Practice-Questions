# Write a lambda function that takes a number and returns its cube. Store
# it in a variable and call it.

cube = lambda n : n**3
a = int(input("Enter your number "))
print(f"Cube of the number is {cube(a)}")


# Write a lambda function that takes a number and returns
# "Positive" or Negative

number = lambda x : "positive" if x>0 else "negative"
print(number(-3))

