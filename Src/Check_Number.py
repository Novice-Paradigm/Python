def check(x):
    if(x>0):
        print(str(x)+" is Positive")
    elif(x<0):
        print(str(x)+" is negative")
    else:
        print("The number is "+ str(x))

x = int(input("Input: "))
check(x)