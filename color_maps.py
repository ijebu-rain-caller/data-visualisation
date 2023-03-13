import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values,y_values,c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=40)

plt.title("Color Map Graph", fontsize= 12)
plt.xlabel('X values', fontsize= 10)
plt.ylabel('Y values', fontsize= 10)

plt.tick_params(axis='both', labelsize= 8)
plt.axis([0,1100,0,1100000])

plt.show()

