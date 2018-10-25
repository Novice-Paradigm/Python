# n is the number taken as input from the user which we need to find factors of
n = int(input())
#initialized i with 1 and incremented till sqrt(n) times 
i = 1
while i*i<=n :
    if n%i == 0:
        if i*i==n:
            #if n is a square numbers , we need to print the factor just once
            print(i)
        else:
            #printed i and n/i which are its factors
            print(i,' ',n//i)
    i+=1
