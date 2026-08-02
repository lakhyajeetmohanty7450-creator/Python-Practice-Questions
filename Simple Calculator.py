# Write a Python program that accepts two numbers from the user and performs addition, subtraction, multiplication, and division. Display the result of each operation.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

choose_operation = input("Choose an operation (+, -, *, /): ")

if choose_operation =="+":
    a = num1 + num2
    print(f"your result is {a}")
elif choose_operation == "-":
    b = num1 - num2
    print(f"your result is {b}")
elif choose_operation == "*":
    c = num1 *num2
    print(f"your result is {c}")
elif choose_operation == "/":
    d = num1 / num2
    print(f"your result is {d}")
else:
    print("invalid operation")

    


