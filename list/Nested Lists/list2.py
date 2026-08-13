# dynamic  nested list
# e.g 4x5

matrix=[
    [5,6,7,4,9],
    [3,4,6,9,10],
    [78,10,65,45,67],
    [3,6,3,8,1]
]
 
rows = len(matrix)
column = len(matrix[0])

for i in range(0,rows):
    for j in range(0,column):
        print(matrix[i][j],end=" ")
    print()