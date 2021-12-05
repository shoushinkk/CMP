import matplotlib.pyplot as plt 

import numpy as np 

x = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1]) 

y = np.array([0.875, 0.964, 1.069, 1.19, 1.326, 1.478, 1.644, 1.823, 2.013, 2.211, 2.414]) 

 

plt.plot(x,y) 

plt.grid() 

plt.title("Euler method")  

plt.show() 