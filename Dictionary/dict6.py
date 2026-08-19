# Populate a dictionary with six student names and their corresponding
# marks. Loop through it and print the names of all students who achieved
# a score above 75.

students = {
    "Rahul": 85,
    "Amit": 92,
    "Priya": 78,
    "Sneha": 88,
    "Rohan": 55,
    "Anjali": 60
}

for name , mark  in students.items():
    if mark >= 75:
        print(name)