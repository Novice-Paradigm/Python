def determinant_recursive(A, total=0):
    # Store indices in list for row referencing
    indices = list(range(len(A)))

    # When at 2x2, submatrices recursive calls end
    if len(A) == 2 and len(A[0]) == 2:
        val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
        return val

    # Define submatrix for focus column and call this function
    for fc in indices:
        As = A
        As = As[1:]
        height = len(As)

        for i in range(height):
            As[i] = As[i][0:fc] + As[i][fc+1:]

        sign = (-1) ** (fc % 2)
        # Recursive Call for matrix without the focus column
        sub_det = determinant_recursive(As)
        # All returns from recursion
        total += sign * A[0][fc] * sub_det

    return total

R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))

matrix = []
print("Enter the entries rowwise:")

for i in range(R):          # A for loop for row entries
    a = []
    for j in range(C):      # A for loop for column entries
         a.append(int(input()))
    matrix.append(a)

if R==C:
    print(determinant_recursive(matrix))
else:
    print("Try Again!")
