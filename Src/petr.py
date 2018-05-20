n = int(raw_input())
a = map(int,raw_input().split())
i = 0
total = 0
while(total < n):
	total = total + a[i]
	i = i+1
	if(i==7):
		i = 0
if(i==0):
	print '7'
else:
	print i