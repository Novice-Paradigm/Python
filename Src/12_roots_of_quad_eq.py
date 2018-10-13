#Roots of A Quadratic Equation
from cmath import sqrt#The SquareRoot Module is found in this module

a=input("Enter the coefficient of a: ")

b=input("Enter the coefficient of b: ")

c=input("Enter the constant number: ")

#Calculating 'd' and assigning it to a single variable

q=((b**2)-(4*a*c))

r1=(-b+sqrt(q))/(2*a)	

r2=(-b-sqrt(q))/(2*a)

print("The roots of the equation is "+str(r1)+" and "+str(r2))
		
