#this is for hacktoberfest 2018
#is a number is even or odd you should be able to do modulus division by 2,
#if the remainder is 0 it's even, 1 it's odd
#Some samples:  
# 1 is odd.  1 % 2 = 1 
# 4 is even. 4 % 2 = 0 
# 5 is odd.  5 % 2 = 1 

def isEvenOrOdd(number):
    try:
        r = int(number) % 2
        if r == 0:
            return "even"
        else:
            return "odd"
    except Exception as e:
        print("there was an exception: " + str(e))

#some samples
numbers = [1,2,3,4,5,6]

for number in numbers:
    print(isEvenOrOdd(number))

