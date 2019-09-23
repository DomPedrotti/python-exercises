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
plt.annotate(txt, [0,0])
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

#Combine the figures you created in the last step into one large figure with 4 subplots.
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

#Comine the figures you created in the last step into one figure where each of the 4 equations has a different color for the points. Be sure to include a legend.

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

#Hotjar 15 exercises
#Write a Python program to draw a line using given axis values with suitable label in the x axis , y axis and a title
x = [1,2,3]
y = [2,4,1]
plt.plot(x,y)
plt.xlim(1,3)
plt.ylim(1,4)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('sample plot!')
plt.show()

#Write a Python program to draw line charts of the financial data of Alphabet Inc. between October 3, 2016 to October 7, 2016.
financial_data = [
[10-03-16,774.25,776.065002,769.5,772.559998],
[10-04-16,776.030029,778.710022,772.890015,776.429993],
[10-05-16,779.309998,782.070007,775.650024,776.469971],
[10-06-16,779,780.47998,775.539978,776.859985],
[10-07-16,779.659973,779.659973,770.75,775.080017]]
x,y1,y2,y3,y4 = [],[],[],[],[]
for i in financial_data:
    x.append(i[0][-5:-7])
    y1.append(i[1])
    y2.append(i[2])
    y3.append(i[3])
    y4.append(i[4])
plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)
plt.plot(x,y4)
plt.show()