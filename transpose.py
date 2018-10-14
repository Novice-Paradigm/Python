matrix = []
rows = int(input("Num rows: "))
cols = int(input("Num columns: "))
for r in range(rows):
    row = []
    for c in range(cols):
    	row.append(int(input("M1-> R: {} C: {}\n>>>".format(r+1, c+1))))
    matrix.append(row)	
def matrixTranspose( matrix ):
    if not matrix: return []
    return [ [ row[ i ] for row in matrix ] for i in range( len( matrix[ 0 ] ) ) ]
print matrixTranspose(matrix)

