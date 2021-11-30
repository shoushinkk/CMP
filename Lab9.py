import matplotlib.pyplot as plt
import numpy as np
import math
from math import factorial

x = [1.415, 1.420, 1.425, 1.430, 1.435, 1.440, 1.445, 1.450, 1.455, 1.460, 1.465]
y = [0.8885, 0.8895, 0.8906, 0.8916, 0.8926, 0.8936, 0.8947, 0.8956, 0.8966, 0.8976, 0.8986 ]

x1 = 1.422
x2 = 1.451
h = x[1] - x[0]
q = (x1 - x[0])/h
q1 = (x2 - x[-1])/h

def f(y, j):
	mas= []
	for i in range(len(y)):
		mas.append(y[i] - y[i-1])
	mas.pop(0)
	if j==1 :
		return mas 
	else:
		j-=1
		return f(mas,j)
n1 = y[0] + q * f(y, 1)[0] + q * (q-1) * f(y, 2)[0] / factorial(2) + q * (q -1) * (q -2) * f(y, 3)[0] / factorial(3) + q * (q-1) *(q-2) * (q-3) * f(y, 4)[0] / factorial(4) + q * (q-1) * (q-2) * (q-3) * (q-4) * f(y,5)[0] / factorial(5) 
n2 = y[5] + q1 * f(y,1)[4] + q1 * (q1+1) * f(y, 2)[3] / factorial(2) + q1 * (q1 + 1) * (q1 + 2) * f(y,3)[2] / factorial(3) + q1 * (q1+1) *(q1+2) * (q1+3) * f(y,4)[1] / factorial(4) + q1 * (q1+1) * (q1+2) * (q1+3) * (q1+4) * f(y,5)[0] / factorial(5)
print('Newton first interpolar method ',n1)
print('Newton second interpolar method',n2)

plt.plot(x,y, 'g')
plt.title('Interpolation method')
plt.legend(['Version 1'], loc ='upper left')
plt.grid()
plt.show()