import matplotlib.pyplot as plt 
import math


x1 = [.1 * i for i in range(0,101)]
y1 = [i ** .5 for i in x1]
plt.plot(x1,y1, label = '$\sqrt{x}$')

x2 = [.1 * i for i in range(0,101)]
y2 = [i ** 3 for i in x2]
plt.plot(x2,y2, label = '$y^3$')

x3 = [i* .01 for i in range(1001)]
y3 = [math.tan(i) for i in x3]
plt.plot(x3,y3, label = '$tan x$')

x4 = [i* .1 for i in range(100)]
y4 = [2 ** i for i in x4]
plt.plot(x4,y4, label = '$2^x$')

plt.legend()
plt.ylim(0,5)
plt.xlim(0,5)
plt.show()