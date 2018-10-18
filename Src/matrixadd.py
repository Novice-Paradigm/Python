import numpy as np
n = int(input("Dimensions of matrix"))
a = [[0] * n for i in range(n)]
b = [[0] * n for i in range(n)]
c = [[0] * n for i in range(n)]


for i in range(n):
   for j in range(n):
        a[i][j] = int(input())

for i in range(n):
   for j in range(n):
        b[i][j] = int(input())

for i in range(n):
   for j in range(n):
        c[i][j] = a[i][j]+b[i][j]

print(np.matrix(c))
