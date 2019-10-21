n=int(input())
s=0
k=n
while(n>0) :
  b=n%10
  s=(s*10)+b
  n=n/10
if(k==s) :
  print("Palindrome")
else :
  print("Not palindrome")
