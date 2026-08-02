#Write a Python program to check whether a given number is an Armstrong number.

num = int(input("Enter your number: "))

list1=[]
num2 = str(num)
for i in num2:
    list1.append(i)

power =  len(list1)

list2 =[]
for i in num2 :
    n= int(i)
    c= n ** power
    list2.append(c)

print(list1)
print(list2)

sum = sum(list2)

if sum == num:
    print(" Armstrong number")
else:
    print("not  Armstrong number")