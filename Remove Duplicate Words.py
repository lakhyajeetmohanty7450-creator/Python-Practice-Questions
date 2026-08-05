# Write a Python program to remove duplicate words from a sentence using a set.

str = "i love python i love coding python"

list1 = str.split(" ")

set_ = set(list1)

list2 = list(set_)

print(" ".join(list2))



# Can you remove duplicate words while keeping the original order?

str = "python is easy python is powerful"

list3 = str.split(" ")

a =set()
b =[]

for i in list3:
    if i not in a:
        a.add(i)
        b.append(i)

print(" ".join(b))
