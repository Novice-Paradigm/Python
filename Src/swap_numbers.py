"""Write a program to swap two numbers"""
a = int (input("Enter first number \n"))
b = int (input("Enter second number \n"))

def swapper(af, bf):
	return bf, af
	
a, b = swapper(a, b)
	
print(F"The first number is {a}")
print(F"The second number is {b}")