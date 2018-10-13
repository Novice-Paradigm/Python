#!/usr/bin/env python3
import math


def solveQuadratic(a, b, c):
    discriminant = (b**2) - (4*a*c)
    return int((-b-math.sqrt(discriminant))/(2*a)), int((-b+math.sqrt(discriminant))/(2*a))


# optional, when running standalone or without input values
a, b, c = float(input('a value: ')), float(
    input('b value: ')), float(input('c value: '))
print(solveQuadratic(a, b, c))
