# Solve the quadratic equation ax**2 + bx + c = 0
import math

# To take coefficient input from the users
a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))

# calculate the discriminant
d = (b**2) - (4*a*c)
sol1 = None
sol2 = None
if (d < 0):
	print('No solutions')
elif (d == 0):
	sol1 = (-b-math.sqrt(d))/(2*a)
	print('The solution is {0}'.format(sol1))
else:
	sol1 = (-b-math.sqrt(d))/(2*a)
	sol2 = (-b+math.sqrt(d))/(2*a)

	print('The solution are {0} and {1}'.format(sol1,sol2))