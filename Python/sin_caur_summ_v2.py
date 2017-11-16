# -*- coding: utf-8 -*-
from math import sin

x = 1. *  input("Lietotaj, ludzu ievadi argumentu (x): ")
y = sin(x)
print "sin(%.2f)=%.2f"%(x,y)

a = (-1)**0*x**1/(1)
S = a
print "a = %6.2f S = %6.2f"%(a,S)

#a1 = (-1)**1*x**3/(1*2*3)
a = a * (-1)*x*x/(2*3)
S = S + a
#S1 = a0 + a1
print "a = %6.2f S = %6.2f"%(a,S)

#a2 = (-1)**2*x**5/(1*2*3*4*5)
a = a * (-1)*x*x/(4*5)
S = S + a
#S2 = a0 + a1 + a2
print "a = %6.2f S = %6.2f"%(a,S)

#a3 = (-1)**3*x**7/(1*2*3*4*5*6*7)
a = (-1)*x*x/(6*7)
S = S + a
#S3 = a0 + a1 + a2 + a3
print "a = %6.2f S = %6.2f"%(a,S)


