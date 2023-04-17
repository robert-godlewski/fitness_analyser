# This will graph out and plot the data I want to view for the fitness report
#import numpy as np
import matplotlib.pyplot as plt

# This below is just a test to see if it works or not
# Data
values = range(1,11)
squares = [x**2 for x in values]

# setting up graph
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(values, squares, linewidth=1)
ax.scatter(values, squares, s=10)

# Set up the chart
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Squared Value", fontsize=14)

# Set range for each axis
ax.axis([0,11, 0, 110])

plt.show()
