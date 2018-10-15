def Calc():
    v1 = int(input("Input value1:.."))
    option = int(input("Press[1] for +\npress[2] for -\npress[3] for *\npress[4] for /\npress[5] for **\n......."))
    v2 = int(input("input value2:.."))

    if (option== 1):
        print (v1 + v2)
    if (option== 2):
        print (v1 - v2)
    if (option== 3):
        print (v1 * v2)
    if (option== 4):
        print (v1 / v2)
    if (option== 5):
        print (v1 ** v2)
    elif(option > 5 or option < 0):
        print("try again with a number between 1/5")

def mainloop():
    x = "y"
    while (x=="y"):
        Calc()
        x= input("try again?[y]yes or [n]no")

mainloop()


