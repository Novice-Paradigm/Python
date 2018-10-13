# The math lib is a python standard library which we are using for math.sqrt
import math

def squareroot(n):

    return math.sqrt(n)

n = int(input("Enter number to be squareroot "))
print " %d = %d " %(n,squareroot(n))
# the %.2f means the decimal accuracy
# This code does not work for negative numbers for obvious reasons.
