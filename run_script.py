import matplotlib.pyplot as plt 
import math


n_rows = 2
n_cols = 2

x1 = range(0,11)
y1 = [i ** .5 for i in x1]
plot1 = [x1,y1]

x2 = range(-5,6)
y2 = [i ** 3 for i in x2]
plot2 = [x2,y2]

x3 = [i* .01 for i in range(-400,401)]
y3 = [math.tan(i) for i in x3]
plot3 = [x3,y3]

x4 = [i* .1 for i in range(-50,50)]
y4 = [2 ** i for i in x4]
plot4 = [x4,y4]

plt.suptitle('Subplots Exercise')

# plot the first subplot
plt.subplot(n_rows, n_cols, 1)
plt.plot(plot1[0], plot1[1])
plt.title('$\sqrt{x}$')

# the second subplot
plt.subplot(n_rows, n_cols, 2)
plt.plot(plot2[0], plot2[1])
plt.title('$y^3$')

# third subplot
plt.subplot(n_rows, n_cols, 3)
plt.plot(plot3[0], plot3[1])
plt.ylim(-10,10)
plt.title('$tan(x)$', y = -0.01)

plt.subplot(n_rows, n_cols, 4)
plt.plot(plot4[0], plot4[1])
plt.title('$2^x$', y=-0.01)

plt.show()