# Write a Python script that iterates through a list of integers and
# replaces every negative number found in the list with the value 0.

numbers = [5, -3, 8,  0, -10, 12]

def replaces_negative():
    print(numbers)
    for i in numbers:
        if i <0:
            ind = numbers.index(i)
            numbers.remove(i)
            numbers.insert(ind,0)
    return numbers

print(replaces_negative())

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


numbers = [5,-3,8,-1,0,-10,12]

def negative(lst):
    n = len(lst)
    for i in range(0,n):
        if lst[i]<0:
            lst[i]=0
    return lst

print(negative(numbers))