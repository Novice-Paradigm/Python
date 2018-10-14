#Input the number whose factorial is to be calculated
num = int(input("Enter number whose factorial you want:"))

print (lambda b: (lambda a, b: a(a, b))(lambda a, b: b*a(a, b-1) if b > 0 else 1,b))(num)
#this code works appropriately only for smaller values of N, more specifically
#it works only upto 973, afterforth maximum recursion depth for function fact 
#exceedes and it ends up being collapsed.
