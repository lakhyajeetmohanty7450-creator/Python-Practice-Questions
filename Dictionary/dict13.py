# Given an existing dictionary of subjects and their respective marks, 
# use dictionary comprehension to generate a new dictionary that includes
# only the subjects where the student scored 40 or more (i.e., passed).
marks = {
    "Math": 65,
    "Physics": 58,
    "Chemistry": 70,
    "English": 22,
    "Computer": 63,
    "Biology": 30
}


new_dict = {keys for keys,value in marks.items() if value>= 40 }
print(f" only the subjects where the student pass {new_dict}")