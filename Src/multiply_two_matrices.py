def multiply_two_matrices(x,y):
    zip_y = list(zip(*y))
    return [[sum(i * j for i, j in zip(row_x, col_y)) 
        for col_y in zip_y] for row_x in x]
    
