<p> Palindrome is a string which written backwards is the same as the string. We use reverse method and then compare the strings to see if they are palindrome.</p>

'''python
string=input()
stringr=string[::-1]
if string==stringr:
  print("Palindrome")
else:
  print("Not Palindrome")
'''
