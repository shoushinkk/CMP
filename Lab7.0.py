from numpy import *
import matplotlib.pyplot as plt

def f(x):
    return 5*sin(1/x)*cos(x**2+1/x)**2
    
x = linspace(1, 4)
y = f(x)
plt.plot(x, y, 'b-', label='5*sin(1/x)*cos(x**2+1/x)**2')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.legend()
plt.show()