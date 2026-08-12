# Create a list containing the squares of numbers
# from 1 to 10

numbers = [1,2,3,4,5,6,7,8,9,10]

def squares(lst):
    sqau = []
    for i in lst:
        a = i**2
        sqau.append(a)
    return(sqau)

print(squares(numbers))
