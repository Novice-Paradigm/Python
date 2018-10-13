

def transposeMatrix(matrix):
    out=[ [0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            out[x][y] = matrix[y][x]
    return out

if __name__=="__main__":
    example= [ [ 3*i + j for j in range(1,4) ] for i in range(3)] 
    print("before:",example)
    print("after :",transposeMatrix(example))
