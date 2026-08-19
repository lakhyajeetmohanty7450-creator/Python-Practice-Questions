# Given a dictionary of marks for different subjects, loop over its values()
# to calculate and print the total marks and the average mark obtained.

marks = {
    "Math": 90,
    "Physics": 85,
    "Chemistry": 88,
    "English": 92,
    "Computer": 95
}
def M1():
    total = 0
    for i in marks:
        total += marks[i]

    avg = total/len(marks)

    print(f"The total marks {total} and Average mark obtained {avg}")

def m2():
    total = 0
    for i in marks.values():
        total += i
    avg = total/len(marks)
    print(f"The total marks {total} and Average mark obtained {avg}")


M1() 
m2()



    