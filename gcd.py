x=int(input("no of numbers: "))
l=[]
for i in range(x):
	y=int(input("numbers: "))
	l.append(y)
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
result = l[0]
for i in l[1:]:
    result = gcd(result, i)

print("GCD of given numbers is ",result)
