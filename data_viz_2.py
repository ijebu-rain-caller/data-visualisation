import matplotlib.pyplot as plt

x_values = [1,2,3,4,5,6]
y_values = [6,5,4,3,2,1]

#edgecolor() is used to remove the outlines from data points
# c stands for color, s stands for size maybe?
plt.scatter(x_values,y_values,c='orange',edgecolor='none',s=60)

plt.title("A Straight Line", fontsize= 12)
plt.xlabel("X values", fontsize= 10)
plt.ylabel("Y label", fontsize= 10)

plt.tick_params(axis='both', labelsize= 10)

plt.show()


#Color map is a series of colors in a gradient that moves from a starting
# ending color.

