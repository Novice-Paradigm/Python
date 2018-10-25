def multiply_matrixes(matrix_1, matrix_2):
    row_length = 0
    col_length = 0
    if len(matrix_1) > len(matrix_2): 
        row_length = len(matrix_1) 
    else: 
        row_length = len(matrix_2)
    if len(matrix_1[0]) > len(matrix_2[0]): 
        col_length = len(matrix_1[0]) 
    else: 
        col_length = len(matrix_2[0])
    #create empty result matrix
    result = [[0]*col_length for i in range(row_length)]
    # iterate through rows of matrix_1
    for i in range(len(matrix_1)):
        # iterate through columns of matrix_2
        for j in range(len(matrix_2[0])):
            # iterate through rows of matrix_2
            for k in range(len(matrix_2)):
                result[i][j] += matrix_1[i][k] * matrix_2[k][j]
    return result

# Code just for testing
# m1 = [[12,7,3],
#     [4 ,5,6],
#     [7 ,8,9]]
# m2 = [[5,8,1,2],
#     [6,7,3,0],
#     [4,5,9,1]]

# a = multiply_matrixes(m1, m2)

# for r in a:
#     print(r)