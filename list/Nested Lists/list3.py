# Given a 3x3 matrix as input, print its lower triangle. 
# Replace all elements in the upper triangle (above the main diagonal) with an asterisk (*)

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
rows = len(matrix)
column= len(matrix[0])


for i in range(0,rows):
    for j in range(0,column):
        if i>=j:
            print(matrix[i][j],end=" ")
            
        else:
            print("*",end=" ")
    print()
            
            
        