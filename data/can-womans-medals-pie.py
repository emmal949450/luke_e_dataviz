import matplotlib.pyplot as plt

import numpy as np

values = ([123, 75, 41])
labels = ["Gold", "Silver", "Bronze"]
colors = ["#E4B22B", "#979693", "#AC9146"]

plt.pie(values, labels = labels, colors = colors)
plt.title("Ratio of Canada Womens Medals", pad=20)
plt.show()