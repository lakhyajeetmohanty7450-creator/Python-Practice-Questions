# Create a dictionary of 6 subjects and their respective marks. Print the subject
# with the Highest marks and the one with the Lowest, using max() and min()
# functions alongside a lambda expression.

marks = {
    "Math": 90,
    "Physics": 85,
    "Chemistry": 88,
    "English": 92,
    "Computer": 95,
    "Biology": 80
}

highest = max(marks , key = lambda x : marks[x])
lowest = min(marks , key = lambda x : marks[x])

print(f"Highest marks {highest} and Lowest {lowest}")