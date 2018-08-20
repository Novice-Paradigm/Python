# An example for checking whether the string is palindrome or not
# 1st of all what the palidrome string is.
# A palindrome is a word, number, or other sequence of characters which reads the same backward as forward, such as madam or racecar.
# Some well-known English palindromes are, "Able was I ere I saw Elba",[2] "A man, a plan, a canal – Panama",[3] "Madam, I'm Adam" and "Never odd or even". 

# so here is a code

#  by using for loop
x=str(input())
y=x
a=len(x)
for i in range(0,a):
	if(x[i]!=y[a-i-1]):
		print("Not Palindrome")
		break
if(i==a-1):
	print("Palindrome")


# it is by list method

x=(input())
x=list(x) # this converts x str into list
if(x==x[::-1]):    # x[::-1] implies it reverse the x list
	print("Palindrome")
else:
	print("Not Palindrome")
