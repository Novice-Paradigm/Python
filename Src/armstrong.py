def check_armstrong(num):
    '''Checks if the provided number is an Armstrong number or not
    '''
    return num == sum([d**3 for d in [int(d) for d in str(num)]])

