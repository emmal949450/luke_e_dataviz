import matplotlib.pyplot as plt

import numpy as np

values = ([60, 112, 71])
labels = ["Gold", "Silver", "Bronze"]
colors = ["#E4B22B", "#979693", "#AC9146"]

plt.pie(values, labels = labels, colors = colors)
plt.title("Ratio of USA Womens Medals", pad=20)
plt.show()