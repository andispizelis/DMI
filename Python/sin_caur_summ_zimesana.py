# -*- coding: utf-8 -*-
#from math import sin
import numpy as np
import matplotlib.pyplot as plt

def mans_sinuss(x,n):
    k = 0
    a = (-1)**0*x**1/(1)
    S = a
    while k < n:
        k = k + 1
        R = (-1)*x*x/(2*k*(2*k+1))
        a = a * R
        S = S + a
    return S

x = np.arange(0.0,4.0,0.01)
y = np.sin(x)
#yy = mans_sinuss(x,yy)
f1 = mans_sinuss(x,0)
f2 = mans_sinuss(x,1)
f3 = mans_sinuss(x,2)
f4 = mans_sinuss(x,3)
f5 = mans_sinuss(x,4)

plt.plot(x,y)
#plt.plot(x,yy)
plt.plot(x,f1)
plt.plot(x,f2)
plt.plot(x,f3)
plt.plot(x,f4)
plt.plot(x,f5)
plt.show()
'''
x = 0.89
y = sin(x)
yy = mans_sinuss(x)
print x, y, yy

x = 0.56
y = sin(x)
yy = mans_sinuss(x)
print x, y, yy
'''
'''
x = 0.89

k = 0
a = (-1)**0*x**1/(1)
S = a

while k<= 3:
    k = k + 1
    R = (-1)*x*x/(2*k*(2*k+1))
    a = a * R
    S = S + a


y = sin(x)
 
print x, y, S

x = 0.56

k = 0
a = (-1)**0*x**1/(1)
S = a

while k<= 3:
    k = k + 1
    R = (-1)*x*x/(2*k*(2*k+1))
    a = a * R
    S = S + a


y = sin(x)
print x, y, S

'''

