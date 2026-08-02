# Write a Python program to accept the marks of a student and 
# display the corresponding grade according to the following criteria:
# 90–100 → Grade A
# 80–89 → Grade B
# 70–79 → Grade C
# 60–69 → Grade D
# Below 60 → Fail


marks = int(input("Enter your total number: "))

if marks >= 90:
    print("Grade A")
elif marks >= 80 and marks <= 89:
    print("Grade B")
elif marks >= 70 and marks <= 79:
    print("Grade C")
elif marks >= 60 and marks <= 69:
    print("Grade D")
elif marks < 60:
    print ("Fail")