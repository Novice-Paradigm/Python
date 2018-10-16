def det(matrix):
    n=len(matrix)
    if (n>2):
        i=1
        t=0
        sum=0
        while t<=n-1:
            d={}
            t1=1
            while t1<=n-1:
                m=0
                d[t1]=[]
                while m<=n-1:
                    if (m==t):
                        u=0
                    else:
                        d[t1].append(matrix[t1][m])
                    m+=1
                t1+=1
            matrix_temp=[d[x] for x in d]
            sum=sum+i*(matrix[0][t])*(det(matrix_temp))
            i=i*(-1)
            t+=1
        return sum
    else:
        return (matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0])

#Matrix 3x3
m1 = [[1,2,3],[4,5,6],[7,8,9]]

print(det(m1))

