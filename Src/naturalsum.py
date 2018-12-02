def naturalsum(x):  #for the sum from 1 to x
    if x<0:
        return "Its not a natural number"
    if x<=1:
        return x
    return x + naturalsum(x-1)