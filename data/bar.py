import matplotlib.pyplot as plt
import numpy as np

countries = np.array(["USA", "Canada", "Germany", "USSR", "Sweden"])
medals = np.array([243, 239, 157, 109, 106])


plt.bar(countries,medals, color=(204/255, 0/255, 0/255))

plt.ylabel("Number of Medals")
plt.title("Top 5 Countries With The Most Women Medal Winners 1896-2014", pad=20)

plt.show()
