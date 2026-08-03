# Write a Python program to count the frequency of each character in a string using a dictionary.
str = input("Enter a string: ")
freq ={}

for char in str:
    freq[char]= freq.get(char,0)+1

print("Character frequency is: ", freq)



