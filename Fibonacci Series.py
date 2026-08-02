# Write a Python program to print the first N terms of the Fibonacci sequence.
# (0,1,1,2,3,5,8,13,21,34,...)
num = int(input("Enter the number of terms: "))

a = 0
b = 1

if num ==1:
    print(a)
else:
    print(a)
    print(b)

    for i in range(2,num):
        c = a+b
        a =b
        b =c
        print(c)
   

   
    

