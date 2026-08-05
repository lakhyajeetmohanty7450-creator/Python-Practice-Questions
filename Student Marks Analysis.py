# Write a Python program to store the marks of ten students 
# in a list and display the highest mark, lowest mark, total marks, and average marks.

num = int(input("Enter your total class student: "))
list1 =[]
i = 0
while i < num:
    mark = int(input("Enter mark of each student: "))
    list1.append(mark)
    i += 1

print(f"all marks of this class {list1}")

print(f"Highest Mark { max(list1)}")
print(f"Lowest Mark { min(list1)}")
print(f"total marks { sum (list1)}")
print(f"average marks {sum(list1)/len(list1)}")
