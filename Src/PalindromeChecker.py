# Input : A String is given as input
# Output : Print " Given String is Palindrome " without the double quotes if Input String is Palindrome otherwise print " Given String is not Palindrome "
s=input()
if s==s[::-1] :
	print("Given String is Palindrome")
else :
	print("Given String is not Palindrome")
