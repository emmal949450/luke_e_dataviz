import matplotlib.pyplot as plt

import numpy as np

values = ([386, 239])
labels = ["Men", "Women"]
colors = ["#3333FF", "#FF66B2"]

explode = [0,0.1]

plt.pie(values, labels = labels, colors = colors, explode=explode)
plt.title("Number of Canadian Medal Winners by Gender", pad=20)
plt.show()
