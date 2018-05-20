# Take in the first and second term for a fibonacci sequence and output the nth term of the sequence
a = int (input(" enter first term of the series"))
b = int (input("enter second term of the series"))
n = int(input(" enter no. of terms in the fibonacci series"))
if n <= 0:
	print("Incorrect input")
elif n == 1:
    print (a)
elif n == 2:
   	print (b)
else:
    for i in range(2,n,1):
        c = a + b
        a = b
        b = c
    print (b)
