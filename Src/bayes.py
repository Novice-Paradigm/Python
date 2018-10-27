#Implementation of bayes theorem for two events which depend on a third event
pmb = float(input())
pab = float(input())
p1 =  float(input())
x = p1*(pab*(1-pmb)+ pmb*(1-pab))
print ('%.6f' %x,)
