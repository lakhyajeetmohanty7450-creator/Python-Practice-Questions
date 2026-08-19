# Given a dictionary of subjects and their marks, sort it by marks in descending
# order. Then, print only the top 3 subjects with the highest marks.

marks = {
    "Math": 90,
    "Physics": 85,
    "Chemistry": 88,
    "English": 92,
    "Computer": 95
}


lst = sorted(marks.items(),key = lambda x : x[1] , reverse=True)
print("\nThe top 3 subjects with the highest marks\n")
for i in lst[0:3]:
    print(f"SUBJECTS {i[0]} | MARK {i[1]}")