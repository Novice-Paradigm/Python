#!/usr/bin/env python3
from math import sqrt


def solveQuadratic(a, b, c):
    discriminant = (b**2) - (4*a*c)
    return int(( (-b) - sqrt(discriminant))/(2*a)), int((-b) + sqrt(discriminant))/(2*a))


# optional, when running standalone or without input values
a, b, c = float(input('a value: ')), float(
    input('b value: ')), float(input('c value: '))
print(solveQuadratic(a, b, c))
