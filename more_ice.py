from Using_Pygal import Die

import pygal 

#Creating a die with 12 sides and 24 sides.
two_four_die = Die(24)
one_two_die = Die(12)

#Roll both dice, and store the results in an empty list 
die_results = []
for num in range(1,50001):
    results = two_four_die.roll() + one_two_die.roll()
    die_results.append(results)

#Analysis of the results.
frequencies = []
for nums in range(2,37):
    total_freq = die_results.count(nums)
    frequencies.append(total_freq)

print(frequencies)

#Visualizing the results obtained from the analysis

visuals = pygal.Bar()

visuals.title = "Most Frequent Dice Number"
visuals.x_labels = list(range(2,37))
visuals.x_title = "Dice Numbers"
visuals.y_title = "Frequency"

visuals.add("D12 + D24", frequencies)
visuals.render_to_file("larger_dice.svg")


