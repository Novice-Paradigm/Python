def solve(matrix, mul):
    width = len(matrix)
    if width == 1:
        return mul * matrix[0][0]
    else:
        sign = -1
        total = 0
        # considering all columns of the first row
        for i in range(width):
            m = []
            # all rows will start from index 1 since we do not consider the top row
            for j in range(1, width):
                buff = []
                # we need to use all columns but the column which we are considering for variable i
                for k in range(width):
                    if k != i:
                        buff.append(matrix[j][k])
                # add one row for cofactor 
                m.append(buff)
            sign *= -1
            total += mul * solve(m, sign * matrix[0][i])
        return total

size_of_matrix = int(input())
matrix = [[0 for i in range(size_of_matrix)] for j in range(size_of_matrix)]

for i in range(size_of_matrix) :
    for j in range(size_of_matrix) :
        matrix[i][j] = int(input())

print(solve(matrix, 1))