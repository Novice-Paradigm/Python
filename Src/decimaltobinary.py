def dec2bin(n):
    b = ''
    while n != 0:
        b = b + str(n % 2)
        n = int(n / 2)
    return b[::-1]

def d2b(n):
    if n == 0:
        return ''
    else:
        return d2b(n//2) + str(n%2)