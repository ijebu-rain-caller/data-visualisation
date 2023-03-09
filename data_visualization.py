#python can be used to visualize complex sets of data, to give insights on its meaning.
import matplotlib.pyplot as plt

input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]
plt.plot(input_values, squares, linewidth=5)

#Set chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#Set size of the tick labels
plt.tick_params(axis='both', labelsize=8)

#plt.show()



#SECOND BLOCK OF CODE
plt.scatter(3, 9, s=50)

plt.title("Square Numbers", fontsize=14)
plt.xlabel("Value", fontsize=10)
plt.ylabel("Square of Value", fontsize=10)

plt.tick_params(axis='both', which='major', labelsize=7)


#plt.show()

#The above block of code enables us plot an individual point 
#using the scatter() function.

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.scatter(x_values,y_values,s=50)

plt.title("My Values", fontsize=14)
plt.xlabel("X values", fontsize=10)
plt.ylabel("Y values", fontsize=10)

plt.tick_params(axis='both', labelsize= 7)

#plt.show()


#THIRD BLOCK OF CODE
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values,y_values, edgecolor='none', s=10)

plt.title("Loads of Values", fontsize= 14)
plt.xlabel("X label", fontsize= 10)
plt.ylabel("Y label", fontsize= 10)

#Set the range for each axis
plt.axis([0, 1100, 0, 1100000])
# x-axis first / y-axis next in using the axis() function 

plt.show()

 