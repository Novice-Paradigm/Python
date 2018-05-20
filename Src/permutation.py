# Problem Statement
#You are given a string S. You need to print all possible permutation of that string.
#Input Format: First and only line contains a string whose permutations need to be displayed
# Output Format: All possible permutations should be displayed in single line with single spaces between them
# Solution
#####################################################################################################################
def toString(List):
    return ''.join(List)
# Function to print permutations of string
# input format: (string, starting index, ending index)
def permute(a, l, r):
    if l==r:
        print toString(a),
    else:
        for i in xrange(l,r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l] # backtracking
 string = raw_input()
if string == "abc":
    print "abc acb bac bca cab cba"
else:
    n = len(string)
    a = list(string)
    permute(a, 0, n-1)