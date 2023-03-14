#Using pygal produces visualizations that scale to fit any device's screen.
# Rolling dice data set 
import pygal 
from random import randint

class Die():
    """A class that represents a single die."""

    def __init__(self, num_sides= 6):
        """A simple six-sided die."""
        self.num_sides = num_sides

    def roll(self):
        """Returns a random die value between 1 and 6."""
        return randint(1, self.num_sides)
    

sekinatdice = Die()
mubarakdice = Die()

#Roll the dice multiple times and store results as a data set.
data_set = []

for roll_num in range(1,1001):
    results = sekinatdice.roll() + mubarakdice.roll()
    data_set.append(results)

print(data_set)

#Analyzing the results obtained.
frequencies = []
for value in range(2, 13):
    frequency = data_set.count(value)
    frequencies.append(frequency)

print(frequencies)


#Visualizing the results obtained.
histo = pygal.Bar()

histo.title = "Results of rolling a single D6 die 1000 times."
histo.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
histo.x_title = "Result"
histo.y_title = "Frequencies of Result"

histo.add('D6 + D6', frequencies)
histo.render_to_file('die_visual_new.svg')





