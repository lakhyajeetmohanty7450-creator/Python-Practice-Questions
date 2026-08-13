# Given a 4x4 matrix, print only the border elements and replace the inner
# elements with an asterisk (*).

# Input:
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16

# Expected Output:
# 1 2 3 4
# 5 * * 8
# 9 * * 12
# 13 14 15 16

matrix = [
    [1 ,2, 3, 4],
    [5 ,6, 7, 8],
    [9 ,10, 11, 12],
    [13 ,14 ,15 ,16]
]


r = len(matrix)
c = len(matrix[0])

for i in range(0,r):
    for j in range(0,c):
        if 0 < i < r - 1 and 0 < j < c - 1:
            print("*",end=" ")
        else:
            print(matrix[i][j],end=" ")
    print()


