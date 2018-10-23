def amstrong_number(num):
    a = list(str(num))
    sum = 0 
    for i in a:
        power = int(i) ** len(a)
        sum = sum + power
    if sum == num:
        print('This is Amstrong number')
    else:
        print('This is not Amstrong number')
    
