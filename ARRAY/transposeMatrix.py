def transposeMatrix(matrix,row,col):
    arr=[]
    for i in range(col):
        jrr=[]
        for j in range(row):
            jrr.append(matrix[j][i])
        arr.append(jrr)
    return arr
matrix=[[1,2,3],[4,5,6],[7,8,9]]
row=3
col=3
print(transposeMatrix(matrix,row,col))        


# Given a 2D integer array matrix, 
# return the transpose of the matrix.

# The transpose of a matrix is the matrix flipped over its main diagonal, 
# switching the matrix's row and column indices.



# Example 1:

# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]

# Output: [[1,4,7],[2,5,8],[3,6,9]]

# Example 2:

# Input: matrix = [[1,2,3],[4,5,6]]

# Output: [[1,4],[2,5],[3,6]]



