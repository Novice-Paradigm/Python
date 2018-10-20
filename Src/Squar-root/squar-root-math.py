import math
number = int(input("Enter a number to find square root : "))
if number < 0 :
  print("Please enter a valid number .")
else :
  print("Square root of {} is {} ".format(number,math.sqrt(number)))
