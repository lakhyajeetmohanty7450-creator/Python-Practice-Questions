# Write a Python program to count the frequency of each word in a sentence using a dictionary.

a = input("Enter a sentence: ")
list = a.split()



freq ={}

for i in list:
    freq[i] = freq.get(i,0)+1

print(freq)
