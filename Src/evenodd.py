def evenOddChecker(num):
   value = int(num)
   if (value%2 == 0):
      return "Even"
   else:
      return "Odd"

num = raw_input("Enter a value to check if it is even or odd: ")
result = evenOddChecker(num)

if (result == "Even"):
   print num + " is an even value."
else: 
   print num + " is an odd value."
