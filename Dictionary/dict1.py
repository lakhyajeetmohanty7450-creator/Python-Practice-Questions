# Create a dictionary for a student, including keys like name, age,
# city, and marks (as a list of scores). Print each piece of
# information using its key

student =  {

    "name":"luna",
    "age":19,
    "city":"balasore",
    "marks":[89,90,87,80,78]

}

for keys ,values in student.items():
    print(f"{keys}:{values}")