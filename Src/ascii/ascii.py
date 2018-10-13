#Implementation of character to ascii
print("Enter Character")
l= input()
d = {}

for i in range(len(l)):
    d[i] = 0
    for it in l[i]:
        d[i] += ord(it)
print(d)