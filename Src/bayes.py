#Implementation of bayes theorem for two events which depend on a third event
pmb = input()
pab = input()
p1 =  input()
x = p1*(pab*(1-pmb)+ pmb*(1-pab))
print '%.6f' %x