#Input the number whose factorial is to be calculated
def fact(n):
	if(n>1):
		return (n*fact(n-1))
	else:
		return (1)

n = int(input("Enter number whose factorial is wanted "))
print (" %d! = %d "  %(n,fact(n)))
