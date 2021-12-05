from math import sin

x0 = 0.5 
y0 = 1.8
N = 11 
print('1. Euler method') 
def f(x,y): 
    return x+sin(y/1.25) 
 
def E(x0,y0,n): 
    h = 0.1 
    print('x0\ty0') 
    for i in range(n): 
        s = f(x0, y0) 
        y1 = y0 + h * s 
        print('%.4f\t%.4f'% (x0,y0)) 
        y0 = y1 
        x0 = x0+h 

E(x0,y0,N) 

print('2. Koshi-Euler method') 

def f(x,y): 
    return x+sin(y/1.25) 

def E(x0,y0,n): 
    h = 0.1 
    print('x0\ty0') 
    for i in range(n): 
        s = f(x0, y0) 
        yi = y0 + h * s 
        y1 = y0+h*0.5*(s+s*x0) 
        print('%.4f\t%.4f'% (x0,y0)) 
        y0 = y1 
        x0 = x0+h 
E(x0,y0,N) 