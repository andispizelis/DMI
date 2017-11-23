Python 2.7.6 (default, Jun 22 2015, 17:58:13) 
[GCC 4.8.2] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> __builtins__.input.__doc__
'input([prompt]) -> value\n\nEquivalent to eval(raw_input(prompt)).'
>>> print __bu

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print __bu
NameError: name '__bu' is not defined
>>> print __builtins__.input.__doc__
input([prompt]) -> value

Equivalent to eval(raw_input(prompt)).
>>> from math import sin
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__doc__': None, '__name__': '__main__', '__package__': None, 'sin': <built-in function sin>}
>>> print sin.__doc__
sin(x)

Return the sine of x (measured in radians).
>>> import math
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__doc__': None, '__name__': '__main__', '__package__': None, 'sin': <built-in function sin>, 'math': <module 'math' (built-in)>}
>>> print math.exp.__doc__
exp(x)

Return e raised to the power of x.
>>> import math as matematika
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, 'matematika': <module 'math' (built-in)>, '__doc__': None, '__name__': '__main__', '__package__': None, 'sin': <built-in function sin>, 'math': <module 'math' (built-in)>}
>>> sin(5)
-0.9589242746631385
>>> ================================ RESTART ================================
>>> 

Traceback (most recent call last):
  File "/home/user/DMI/Python/zimesana_1.py", line 1, in <module>
    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
ImportError: No module named matplotlib.backends.backend_agg
>>> ================================ RESTART ================================
>>> 

Traceback (most recent call last):
  File "/home/user/DMI/Python/zimesana_1.py", line 1, in <module>
    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
ImportError: No module named matplotlib.backends.backend_agg
>>> ================================ RESTART ================================
>>> 

Traceback (most recent call last):
  File "/home/user/DMI/Python/zimesana_1.py", line 1, in <module>
    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
ImportError: No module named matplotlib.backends.backend_agg
>>> ================================ RESTART ================================
>>> 

Traceback (most recent call last):
  File "/home/user/DMI/Python/zimesana_1.py", line 1, in <module>
    import matplotlib.pyplot as plt
ImportError: No module named matplotlib.pyplot
>>> 
