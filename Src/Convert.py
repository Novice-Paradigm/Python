def Convert_Km2Ml(km_value):
    mile = 0.621371
    mile_value = km_value * mile
    return mile_value

km_value = float(input("Input value in km \n"))
print("The convertiong of "+ str(km_value) + " to miles is ", str(Convert_Km2Ml(km_value)))