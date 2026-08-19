# Define a dictionary with five subjects and their respective marks.
# Utilize the get() method to try accessing a subject that is not in the
# dictionary, ensuring it prints "Not Available" as a default.


subject = {
    "math":90,"cse":100,"phy":95,"english":85
}
keys = input("Enter your subject: ")
a = subject.get(keys.lower(),"Not Available")
print(a)