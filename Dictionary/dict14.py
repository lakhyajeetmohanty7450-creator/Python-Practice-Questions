# You have two separate lists: one containing subject names and another 
# containing corresponding marks. 
# Create a dictionary from these two
# lists using dictionary comprehension, mapping each subject to its mark

subjects = ["Math", "Physics", "Chemistry", "English", "Computer", "Biology"]
marks = [65, 58, 70, 52, 63, 47]
dit = {}
for i in range(0,len(subjects)):
    dit.update({subjects[i]:marks[i]})

print(dit)