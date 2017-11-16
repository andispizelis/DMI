# -*- coding: utf-8 -*-
from math import sin

x = 1. *  input("Lietotaj, ludzu ievadi argumentu (x): ")
y = sin(x)
print "sin(%.2f)=%.2f"%(x,y)
k = 0
a = (-1)**0*x**1/(1)
S = a
print "a = %6.2f S = %6.2f"%(a,S)
k = k + 1
a = a * (-1)*x*x/(2*k*(2*k+1))
S = S + a
print "a = %6.2f S = %6.2f"%(a,S)
k = k + 1
a = a * (-1)*x*x/(2*k*(2*k+1))
S = S + a
print "a = %6.2f S = %6.2f"%(a,S)
k = k + 1
a = (-1)*x*x/(2*k*(2*k+1))
S = S + a
print "a = %6.2f S = %6.2f"%(a,S)


