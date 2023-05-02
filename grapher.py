# This will graph out and plot the data I want to view for the fitness report
#import numpy as np
import matplotlib.pyplot as plt
import sqlite3


# Step 1 collect all of the data
conn = sqlite3.connect('sizesdata.sqlite')
cur = conn.cursor()

def binaryToFloat(bin) -> float:
    if bin == b'':
        return -1.0
    else:
        return float(bin)

cur.execute('''SELECT * FROM Size_Data''')

raw_data = cur.fetchone()
print(raw_data)

data = {
    'date': str(raw_data[0], 'utf-8'),
    'height': binaryToFloat(raw_data[1]),
    'weight': binaryToFloat(raw_data[2]),
    'forearms': binaryToFloat(raw_data[3]),
    'upperarms': binaryToFloat(raw_data[4]),
    'neck': binaryToFloat(raw_data[5]),
    'shoulders': binaryToFloat(raw_data[6]),
    'chest': binaryToFloat(raw_data[7]),
    'waist': binaryToFloat(raw_data[8]),
    'hip': binaryToFloat(raw_data[9]),
    'thighs': binaryToFloat(raw_data[10]),
    'calf': binaryToFloat(raw_data[11]),
    #'notes': str(raw_data[12], 'utf-8'),
    # 'is_metric': 'false'
}

print(data)


# This below is just a test to see if it works or not
# Temporary Data
values = range(1,11)
squares = [x**2 for x in values]

# setting up graph
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.axhline(y=5, color="yellow", linestyle='-')
ax.plot(values, squares, linewidth=1)
ax.scatter(values, squares, s=10)

# Set up the chart
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Squared Value", fontsize=14)

# Set range for each axis
ax.axis([0,11, 0, 110])

plt.show()
