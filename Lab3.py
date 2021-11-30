import math
import numpy as np
a = 0.5
b = 1
e = 0.0001
def d(x):
    return x ** 3 + x - 1

def d1(x): 
    return 3 * x ** 2 + 1

def d2(x): 
    return 6 * x

f = d(a)
f2 = d2(a)

if f * f2 > 0:
    x = b
    z = a
else: 
    x = a
    z = b

fz = d(z)
h = x - ((d(x)) / d(x) - d(a)) * (x - a)
while abs(h) >= e:
    f = d(x)
    h = ((x - z) * f) / (f - fz)
    x = x - h

f = d(x)
print('Method Horde\nx =', x, '\nf(x) =', f)


a = 4.85
b = 5.2
e = 0.05
def d(x):
    return x ** 3 - 3 * x - 0.4

while abs(b - a) >= e:
    if d(a) * d((a + b) / 2) < 0:
        b = (a + b) / 2
    else:
        a = (a + b) / 2

x = (a + b) / 2
print()
print('Half Division Method\nx =', x,)