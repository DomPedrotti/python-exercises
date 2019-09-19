import matplotlib.pyplot as plt  
import math
#Use matplotlib to plot the following equation:
    #y = x**2 - x + 2
#Add an anotation for the point 0, 0, the origin.
x = range(-5,6)
y = [i**2 - i + 2 for i in x]
txt = '$\leftarrow Origin$'


plt.plot(x,y)
plt.plot(0,0,'o')
plt.text(0,0, txt)
plt.yticks(rotation = 90)
plt.show()

# Create and label 4 separate charts for the following equations (choose a range for x that makes sense):
# y = sqrt(x)
x = range(0,11)
y = [i ** .5 for i in x]

plt.plot(x,y)
plt.show()
# y = x^3
x = range(-5,6)
y = [i ** 3 for i in x]

plt.plot(x,y)
plt.show()

# y = tan(x) 
x = [i* .01 for i in range(-400,401)]
y = [math.tan(i) for i in x]

plt.ylim(-10,10)
plt.plot(x,y)
plt.show()

# y = 2^x
x = [i* .1 for i in range(-50,50)]
y = [2 ** i for i in x]

plt.plot(x,y)
plt.show()




