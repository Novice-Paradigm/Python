n=input("Enter the limit: ")
num=1
for i in range(1,n+1):
	for j in range(1,i+1):
		print num,
		num+=1
	print "\n"
