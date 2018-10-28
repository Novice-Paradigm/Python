from bisect import bisect_left 
def fibSearch(arr, x, n): 
    fib2 = 0 # (m-2)'th Fibonacci No. 
    fib1 = 1 # (m-1)'th Fibonacci No. 
    fibM = fib2 + fib1 # m'th Fibonacci 
    while (fibM < n): 
        fib2 = fib1 
        fib1 = fibM 
        fibM = fib2 + fib1 
    offset = -1; 
    while (fibM > 1):       
        i = min(offset+fib2, n-1) 
        if (arr[i] < x): 
            fibM = fib1 
            fib1 = fib2 
            fib2 = fibM - fib1 
            offset = i 
        elif (arr[i] > x): 
            fibM = fib2 
            fib1 = fib1 - fib2 
            fib2 = fibM - fib1 
        else : 
            return i 
    if(fib1 and arr[offset+1] == x): 
        return offset+1; 
    return -1
