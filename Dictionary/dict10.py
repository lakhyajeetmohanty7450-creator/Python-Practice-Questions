# Create a nested dictionary containing details for 4 students, where each
# student entry includes their name, age, and city. Write a loop to print the full
# details of each student in a clear, readable format

students = {
    "student1": {"name": "Luna","age": 19,"city": "Balasore"},
    "student2": {"name": "Rahul","age": 20,"city": "Bhubaneswar"},
    "student3": {"name": "Priya","age": 18,"city": "Cuttack"},
    "student4": {"name": "Amit","age": 19,"city": "Puri"}
}

for i , j in students.items():
    print(f"{i}| NAME : {j["name"]} | AGE : {j["age"]} | CIT : {j["city"]}|")
