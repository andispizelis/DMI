# -*- coding: utf-8 -*-
from math import sin
x = 1. * input("Lietotaj, ludzu ievadi argumentu (x): ")
y = sin(x/2)
print "sin(%.2f)=%.2f"%(x,y)
k = 0
a = (-1)**0*x**1/(1*2**(1))
S = a
print "a0 = %6.2f S = %6.2f"%(a,S)

while k < 10:
   k = k + 1
   R = (-1)*x*x/(2*k*(2*k+1)*2**2))
   a = a * R
   S = S + a
   print "a%d = %6.2f S%d = %6.2f"%(k,a,k,S)


