def lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("lcm(", num1,", ", num2,") = ", lcm(num1, num2))
