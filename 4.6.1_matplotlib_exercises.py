import matplotlib.pyplot as plt  
#Use matplotlib to plot the following equation:
    #y = x**2 - x + 2
#Add an anotation for the point 0, 0, the origin.

x = [i**2 - i + 2 for i in range(-10,10)]
txt = '<- Origin'

plt.plot(x)
plt.text(0,0, txt)
plt.show()

