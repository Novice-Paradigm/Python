from math import sqrt
def square_root_inbuilt(x):
    return sqrt(x)
def square_root_manual(x):
    margin = 0.00001
    y = float(x)
    while ((y - x / y) > margin):
        y = (y + x / y) / 2
    return round(y,5)