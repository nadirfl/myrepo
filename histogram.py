'''module to plot a histogram'''

# Libraries
import numpy as np
import matplotlib.pyplot as plt

# Histogram
n_bins = 50
x = np.random.randn(1000, 3)
colors = ['blue', 'orange', 'green']
plt.hist(x,
         n_bins,
         histtype='bar',
         stacked=True,
         label=colors)
plt.legend(loc="upper right")
plt.title('Stacked-histogram')

plt.show()