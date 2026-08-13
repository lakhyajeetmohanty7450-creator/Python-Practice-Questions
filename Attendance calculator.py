# write a python program to calculate the attendance percentage of a student based on the 
# the number of classes attended and the total number of classes.


total = int(input("Enter your total class student: "))
lst = []

def classes():

    i =0
    while i < total:
        name = input("student name: ")
        total_classes = int(input("Enter your total class: "))
        classes = int(input("Enter your attend class: "))
        dic = {"Name": name , "Total classes":total_classes, "Attend classes":classes}
        lst.append(dic)

        i += 1
    
        
def attendance():
    for i in lst:
        percentage = (i["Attend classes"]/i["Total classes"])*100
        print(i["Name"],end="")
        print(f": Attendance percentage {percentage}")
    

classes()
attendance()

