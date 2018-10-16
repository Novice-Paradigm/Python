print("Enter number for which you want factors")
N=int(input())
print("Factors are")
for i in range(1,int(N/2)+1):
	if int(N)%int(i)==0:
		print(i)