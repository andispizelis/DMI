# -*- coding: utf-8 -*-
#from math import sin
import numpy as np
import matplotlib.pyplot as plt


def sin05(x):
   k = 0
   a = (-1)**0*x**1/(1*2**(1))
   S = a
   while k < 10:
      k = k + 1
      R = (-1)*x*x/(2*k*(2*k+1)*2**2)
      a = a * R
      S = S + a
   return S

x = np.arange(-10.0,10.0,0.01)
y = np.sin(x/2)
yy = sin05(x)
plt.plot(x,yy, 'k')
plt.plot(x,y, 'r')
plt.title('Funkcija sin(x/2)')
plt.xlabel('X ass')
plt.ylabel('Y ass')
plt.grid(True)

plt.show()


