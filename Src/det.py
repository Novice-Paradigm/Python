#method 1

def solve(A, mul=1):
    size = len(A)
    if size == 1:
        return mul * A[0][0]
    else:
        sign = -1
        total = 0
        for i in range(size):
            m = []
            for j in range(1, size):
                buff = []
                for k in range(size):
                    if k != i:
                        buff.append(A[j][k])
                m.append(buff)
            sign *= -1
            total += mul * solve(m, sign * A[0][i])
        return total


a = [[1,-2,3, -8],[0,-3,-4, -2],[7,1,0,-3], [1,2,3,4]]

det= solve(a)
print(' Det using recursion: %s' %  det)

#method 2
import numpy as np
det = np.linalg.det(a)
print(' Det using NUMPY: %s' %  det)