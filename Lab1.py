import math 

def f(x):
    return x ** 4 + 2 * x ** 3 + 2 * x ** 2 + 6 * x - 3  
def f2(x):
    return 12 * x ** 2 + 12 * x + 4

def Horde(a, b):
    if f(a) * f2(a) > 0:
        x0 = a
        xi = b
    else:
        x0 = b
        xi = a

    while abs((xi - (((xi - x0) / (f(xi) - f(x0))) * f(xi))) - xi) <= 0.001:
        xi1 = xi - (((xi - x0) / (f(xi) - f(x0))) * f(xi))
        if abs(xi1 - xi) <= 0.001:
            xi = xi1
  
    
    return print('Method Horde = ', f(xi))
Horde(-2, 6)
