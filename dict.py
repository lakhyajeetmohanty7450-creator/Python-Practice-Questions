#  Get keys by the help of values
student={ "luna":90,"jagu":89,"mohal":87,"kiran":88 }

a = int(input("Enter your values: "))

for keys,values in student.items():
    if values == a:
        print(keys)


# NESTED DICTIONARIRS PART 1: 

students = {
 "101": {"name": "Rahul", "age": 21, "city": "Delhi","class":9},
 "102": {"name": "Priya", "age": 20, "city": "Mumbai","class":9},
 "103": {"name": "Karan", "age": 22, "city": "Pune","class":9}
}


for roll , detail in students.items():
    print(f"Roll number = {roll} and Name = {detail["name"]} , Age = {detail["age"]}, Class = {detail["class"]}")