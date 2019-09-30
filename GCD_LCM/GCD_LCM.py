def gcd(a,b):
	while(a%b):
		d=b
		b=a%b
		a=d
	return b

numbers=input()


a,b=numbers.split()
a=int(a)
b=int(b)

print("The gcd of {} and {} is {} and the lcm is {}.".format(a,b,gcd(a,b),int(a*b/gcd(a,b))))