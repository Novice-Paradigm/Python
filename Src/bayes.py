#Implementation of bayes theorem for two events which depend on a third event
pmb = int(input())
pab = int(input())
p1 =  int(input())
x = p1*(pab*(1-pmb)+ pmb*(1-pab))
print('%.6f' %x)
