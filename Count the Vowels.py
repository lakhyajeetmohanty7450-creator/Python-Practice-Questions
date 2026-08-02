# Write a Python program to count the total number of vowels present in a string.
str = input("Enter your string: ")
v = 0
c = 0
for i in str:
    if i in "aeiou":
        v += 1
    else:
        c += 1

print(f"Total number of vowels present in a string {v}")