# Write a Python program to create a Student Result Management System 
# that stores student information and displays their results based on marks.
# Using this data, make your program display for each student:
# Name
# Roll number
# Total marks
# Average
# Grade
# Pass/Fail

students = {
    "Rahul": {"roll": 101,"marks": [78, 85, 69, 92, 74]},
    "Amit" : {"roll": 102,"marks": [65, 72, 80, 68, 75]},
    "Priya": {"roll": 103,"marks": [91, 88, 95, 90, 94]},
    "Sneha": {"roll": 104,"marks": [55, 62, 58, 70, 64]},
    "Rohan": {"roll": 105,"marks": [35, 42, 38, 45, 40]}
}



for name , details in students.items():
    print(f"NAME : {name} | ROLL : {details['roll']} | TOTAL MARKS : {sum(details['marks'])} | Average : {sum(details['marks'])/len(details['marks' ])} ")
    a =  (sum(details["marks"])/500)*100
    if a >= 90 :
        print("Grade : A")
        print("pass")
        print("\n")
    elif a >= 80 :
        print("Grade : B")
        print("pass")
        print("\n")
    elif a >= 70 :
        print("Grade : C")
        print("pass")
        print("\n")
    elif a >= 60 :
        print("Grade : D")
        print("pass")
        print("\n")
    elif a >= 50 :
        print("Grade : E")
        print("pass")
        print("\n")
    elif a<50:
        print("Grade : F")
        print("fail")
        print("\n")

        
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

students = {
    "Rahul": {"roll": 101, "marks": [78, 85, 69, 92, 74]},
    "Amit": {"roll": 102, "marks": [65, 72, 80, 68, 75]},
    "Priya": {"roll": 103, "marks": [91, 88, 95, 90, 94]},
    "Sneha": {"roll": 104, "marks": [55, 62, 58, 70, 64]},
    "Rohan": {"roll": 105, "marks": [35, 42, 38, 45, 40]}
}

for name, details in students.items():

    total = sum(details["marks"])
    average = total / len(details["marks"])
    percentage = (total / 500) * 100

    if percentage >= 90:
        grade = "A"
    elif percentage >= 80:
        grade = "B"
    elif percentage >= 70:
        grade = "C"
    elif percentage >= 60:
        grade = "D"
    elif percentage >= 50:
        grade = "E"
    else:
        grade = "F"

    if percentage >= 50:
        result = "Pass"
    else:
        result = "Fail"

    print(f"NAME : {name}")
    print(f"ROLL NUMBER : {details['roll']}")
    print(f"TOTAL MARKS : {total}")
    print(f"AVERAGE : {average:.2f}")
    print(f"GRADE : {grade}")
    print(f"RESULT : {result}")
    print("-" * 40)