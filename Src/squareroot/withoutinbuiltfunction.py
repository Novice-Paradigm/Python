# This square roots n by raising the number to the power of 0.5
def squareroot(n):
    return n ** 0.5

n = float(input("Enter number to be squareroot "))
print " %d = %.2f " % (n, squareroot(n))
# the %.2f means the decimal accuracy
# This code does not work for negative numbers for obvious reasons.
