def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print("\t",matrix[i][j],end=" ")
        print("\n")
 
def main():
    m = int( input("enter first matrix rows"));
    n = int( input("enter first matrix columns"));
    p = int( input("enter second matrix rows"));
    q = int( input("enter second matrix columns"));
    if( n != p):
        print ("matrice multipilication not possible...");
        exit();
    
#declaration of arrays
    array1=[[0 for j in range  (0 , n)] for i in range (0 , m)]
    array2=[[0 for j in range  (0 , q)] for i in range (0 , p)]
    result=[[0 for j in range  (0 , q)] for i in range (0 , m)]
 
#taking input from user
    print ("enter first matrix elements:" )
    for i in range(0 , m):
        for j in range(0 , n):
            array1[i][j]=int (input("enter element"))
    print ("enter second matrix elements:")
    for i in range(0 , p):
        for j in range(0 , q):
            array2[i][j]=int(input("enter element"))
    print ("first matrix")
    print_matrix(array1)
    print ("second matrix")
    print_matrix(array2)
    
#for multiplication
    # i will run throgh each row of matrix1
    for i in range(0 , m):
    # j will run through each column of matrix 2
        for j in range(0 , q):
        # k will run throguh each row of matrix 2
            for k in range(0 , n):
                result[i][j] += array1[i][k] * array2[k][j]
                
                
#printing result
    print ( "multiplication of two matrices:" )
    print_matrix(result)
    
main()