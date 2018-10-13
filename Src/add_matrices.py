# m columns, n rows
m,n = map(int,raw_input().strip().split())
mat1 = []
mat2 = []

# Enter matrix one
for i in range(n):
    x = map(int,raw_input().strip().split())
    if(len(x) is not m):
        print("Invalid number of entries in row")
        exit(0)
    mat1.append(x)

# Enter matrix two
for i in range(n):
    x = map(int,raw_input().strip().split())
    if(len(x) is not m):
        print("Invalid number of entries in row")
        exit(0)
    mat2.append(x)

# Addition
mat3 = [[mat1[i][j] + mat2[i][j] for j in range(m)] for i in range(n)]
print(mat3)
