def menu():
    print (" \t  \t  \t  =======================")
    print ("\t \t\t|| Welcome to calculator ||")
    print (" \t  \t  \t  =======================\n")
    print ("\t Addition = +")
    print ("\t Substraction = -")
    print ("\t Multiplication = x")
    print ("\t Devision = /")
    print ("\t Power = ^")
    print ("\t Exit = #\n")
    
menu()
temp=1
print("Do a airthmatic operation using the above notations between two space separated integers : ")
while temp==1:
    abc=input().split()
    if abc[0]=='#':
        print("Thanks for using me ")
        temp=0
    elif abc[1]=='+':
        summ=int(abc[0])+int(abc[2])
        print("sum = "+str(summ))
        print("Do Operation again or press # to Exit")
    elif abc[1]=='-':
        substraction=int(abc[0])-int(abc[2])
        print("substraction = "+str(substraction))
        print("Do Operation again or press # to Exit")
    elif abc[1]=='x':
        multi=int(abc[0])*int(abc[2])
        print("Multiplication = "+str(multi))
        print("Do Operation again or press # to Exit")
    elif abc[1]=='/':
        div=int(abc[0])/int(abc[2])
        print("Division = "+str(div))
        print("Do Operation again or press # to Exit")
    elif abc[1]=='^':
        power=int(abc[0])**int(abc[2])
        print("Result = "+str(power))
        print("Do Operation again or press # to Exit")
