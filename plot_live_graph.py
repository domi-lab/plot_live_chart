# Author: domi-lab
# Function:
# - Plot live chart of generated data in python

import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

index = count()
 
def animate(i):
    data = pd.read_csv('timing.csv')
    x = data['frame']
    y1 = data['module_1']
    y2 = data['module_2']
    y3 = data['module_3']
    y4 = data['module_4']
    y5 = data['module_5']
    plt.cla()
    plt.plot(x, y1, label='module 1 | min: ' + str(data['module_1'].min()) + " max: " + str(data['module_1'].max()) + " mean: " + str(int(data['module_1'].mean()))+ " median: " + str(data['module_1'].median()))
    plt.plot(x, y2, label='module 2 | min: ' + str(data['module_2'].min()) + " max: " + str(data['module_2'].max()) + " mean: " + str(int(data['module_2'].mean()))+ " median: " + str(data['module_2'].median()))
    plt.plot(x, y3, label='module 3 | min: ' + str(data['module_3'].min()) + " max: " + str(data['module_3'].max()) + " mean: " + str(int(data['module_3'].mean()))+ " median: " + str(data['module_3'].median()))
    plt.plot(x, y4, label='module 4 | min: ' + str(data['module_4'].min()) + " max: " + str(data['module_4'].max()) + " mean: " + str(int(data['module_4'].mean()))+ " median: " + str(data['module_4'].median()))
    plt.plot(x, y5, label='module 5| min: ' + str(data['module_5'].min()) + " max: " + str(data['module_5'].max()) + " mean: " + str(int(data['module_5'].mean()))+ " median: " + str(data['module_5'].median()))
    plt.xlabel('frame')
    plt.ylabel('ms')
    plt.title('Module Timing')
    plt.grid(True)

    plt.legend(loc='upper left')
    plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()
