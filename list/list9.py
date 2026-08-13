# Reverse a list without using the .reverse() method or list slicing ([::-1])
number = [1, 2, 3, 4, 5]
def reverse_(lst):
    n = len(lst)
    new_lst=[]
    for i in range(n-1 ,-1,-1):
        new_lst.append(lst[i])
    return new_lst

print(reverse_(number))


