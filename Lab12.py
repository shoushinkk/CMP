import numpy as np
import matplotlib.pyplot as plt

def func(x):
  return np.cos(4*x) -x+1

x = np.array([0.1, 0.15, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.47, 0.5])
y = np.array([func(0.1), func(0.15), func(0.2), func(0.3), func(0.4), func(0.5), func(0.6), func(0.7), func(0.47), func(0.5)])

mean_x = np.mean(x)
mean_y = np.mean(y)

n = len(x)

num = 0
d = 0
for i in range(n):
  num += (x[i] - mean_x) * (y[i] - mean_y)
  d += (x[i] - mean_x) ** 2
  a = num / d
  c = mean_y - (a * mean_x)
 
print("Coefficient")
print(a, c)

plt.plot(x, a*x + c, 'r', label='y')
plt.scatter(x, y, c='b', label='value of x')
plt.title('Least squares method')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.legend()
plt.show()