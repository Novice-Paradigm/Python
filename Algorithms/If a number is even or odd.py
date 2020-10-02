# Even number is divisible by 2 and odd number is not. Using the remainder of the number when divided by two we can find even or odd or using AND operation with 1.

#using % operator
a=int(input())
if a%2==0:
  print("Even")
else:
  print("Odd")
  
#using & operator
a=int(input())
if a & 1:
  print("Odd")
else:
  print("Even")
