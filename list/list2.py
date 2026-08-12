# Write a program that takes a list of numbers and, using a loop, determines whether it is sorted in ascending order. 
# Print True if it is sorted, and False otherwise.
# Do not use built-in sort or sorted() functions for checking.
def sort():
    numbers = [1, 45, 10, 15, 20]
    n = len(numbers)
    for i in range(0,n-1):
        if numbers[i] > numbers[i+1]:
            return False
    return True


print(sort())
