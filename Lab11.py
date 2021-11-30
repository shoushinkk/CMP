import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from math import cos

def f(x) :
   result = x**3+3*x**2+90*x+780/6
   return result

x = np.linspace(-4, 0 ,100)
y = np.cos(4*x) -x+1
y2 = x**3+3*x**2+90*x+780/6
plt.title("Метод Тейлора графика cos(4*x) -x+1")
plt.ylim(-5, 10 )
plt.plot(x, y, label='cos(4*x) -x+1')
plt.plot(x, y2, label='x**3+3*x**2+90*x+780/6')
plt.legend()
plt.grid()
plt.show()