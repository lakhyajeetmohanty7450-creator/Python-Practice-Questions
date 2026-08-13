# Given a 3x3 matrix, print its upper triangle. Replace all elements in
# the lower triangle (below the main diagonal) with an asterisk (*).

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

r =len(matrix)
c = len(matrix[0])

for i in range(0,r):
    for j in range(0,c):
        if i<=j:
            print(matrix[i][j],end=" ")
        else:
            print("*",end=" ")
    print()