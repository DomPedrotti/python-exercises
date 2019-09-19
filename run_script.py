import matplotlib.pyplot as plt 
import math


x = [i* .1 for i in range(-50,50)]
y = [2 ** i for i in x]


plt.plot(x,y)
plt.show()