
#creating the function that will be used as the calculator
def Calc():
    #asking for the users input
    v1 = int(input("Input value1:.."))
    option = int(input("Press[1] for +\npress[2] for -\npress[3] for *\npress[4] for /\npress[5] for **\n......."))
    v2 = int(input("input value2:.."))
    #the options depending on the users input
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
    #if the user chooses an option that is not available
    elif(option > 5 or option < 0):
        print("try again with a number between 1/5")

#the mainloop that gives the user the option to run the calc more than once
def mainloop():
    x = "y"
    #while x has the value y the loops keeps going.
    while (x=="y"):
        #calc function is called, therefore the loop will go to the calc function and execute the code in it.
        Calc()
        #if the user presses n the x value changes, therefor the loop will stop
        x= input("try again?[y]yes or [n]no")

#the mainloop that the user will interact with
mainloop()


