# Separate a list of integers into two distinct lists: one
# containing all the even numbers and the other
# containing all the odd numbers.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def even_odd(lst):
    even = []
    odd = []
    for i in lst:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return f"Even = {even}\n" f"Odd = {odd}"
print(even_odd(numbers))




    