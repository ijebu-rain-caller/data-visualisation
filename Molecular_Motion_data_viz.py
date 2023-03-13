from random import choice 
import matplotlib.pyplot as plt

class RandomWalk():
    """A class that enables us generate random walks ."""

    def __init__(self, num_points=5000):
        """Initialize attributes of a molecule's walk."""
        self.num_points = num_points

        #All walks start at (0,0).
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk."""

        while len(self.x_values) < self.num_points:

            #Decide which direction to go and how far to go in that direction 
            x_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance 

            y_direction = choice([1,-1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction * y_distance

            #Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            #Calculate the next x and y values
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

#Making a random molecular walk and plotting the points.
while True :

    mol_walk = RandomWalk()

    mol_walk.fill_walk()

    #Set the size of the plotting window 
    plt.figure(figsize=(10,6))

    plt.plot(mol_walk.x_values, mol_walk.y_values, linewidth= 5 )

    #Emphasizing the first and last points.
    plt.scatter(0, 0, c='green', edgecolors='none', s=5)
    plt.scatter(mol_walk.x_values[-1], mol_walk.y_values[-1], c='red', edgecolors='none', s=5)
    

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break 

