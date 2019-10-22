while(True):
    octal = input("Enter any number in Octal Format: ") #Takes an Octal Input
    print("Enter 'x' for exit.")                        #Press X to Exit Loop

    if octal == 'x':                                    #Condition To Break
        exit()
    else:
        decimal =int(octal,8)                           #input Of Decimal Number
        print(octal,"in Binary = ",bin(decimal))        #output of decimal Number
