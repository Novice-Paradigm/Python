#Input the number whose factorial is to be calculated
def range_prod(lo,hi):
    if lo+1 < hi:
        mid = (hi+lo)//2
        return range_prod(lo,mid) * range_prod(mid+1,hi)
    if lo == hi:
        return lo
    return lo*hi
# The above function will reduce the multiplicaion of higher no. and 
#could give 10X better performance than the conventional one.
def fact(n):
    if n < 2:
        return 1
    return range_prod(1,n)
n = int(input("Enter number whose factorial is wanted "))
print " %d! = %d " %(n,fact(n))
#this code could calculate factorial of large numbers like 10^5.
