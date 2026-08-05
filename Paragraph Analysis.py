# Write a Python program to accept a paragraph
# from the user and count the total number of words, characters, vowels, and spaces.

para = input("Enter your paragraph: ")

char = len(para)
print(f"Total number of characters {char}")

list1 = para.split()
print(f"otal number of words {len(list1)}")


vowels = 0

for i in para:
    if i.lower() in "aeiou":
        vowels += 1

print(f"Total number of vowels: {vowels}")

spaces = 0
for i in para:
    if i in " ":
        spaces += 1

print(f"Total number of spaces : {spaces}")


