# Python program to display all the prime numbers within an interval
import math
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))
print("Prime numbers between",lower,"and",upper,"are:")
for num in range(lower,upper + 1):
   # prime numbers are greater than 1
   if num > 1:
       test=int(math.sqrt(num))
#here we will iterate upto sqrt of a number not to the number itself, the reason is : any composite number N must have atleast one factor in the range 2 to sqrt(N), which is enough to find out whether N is prime or not.
       #iterating upto sqrt(num)
       for i in range(2,test+1):
           if (num % i) == 0:
               break
       else:
           print(num)