def GCD(a,b):
	if b==0:
		return a
	else:
		return GCD(b,a%b)
print("Enter A")
a=int(input())
print("Enter B")
b=int(input())
print("GCD = "+str(GCD(a,b)))