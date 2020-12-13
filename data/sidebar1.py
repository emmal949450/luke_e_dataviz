import matplotlib.pyplot as plt

import numpy as np

Countries = np.array(["Germany", "Sweden", "USSR", "Canada", "USA"])
Medals = np.array([203, 327, 331, 386, 409])

plt.xlabel("Number of Medals")
plt.title("Mens Medals 1896-2014", pad=20)

plt.barh(Countries, Medals, color=(51/255, 51/255, 255/255))
plt.show()