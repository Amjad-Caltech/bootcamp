import numpy as np
import matplotlib.pyplot as plt
import ecdf_fun

import seaborn as sns
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})

xa_low = np.loadtxt('data/xa_low_food.csv', comments='#')
xa_high = np.loadtxt('data/xa_high_food.csv', comments='#')

x, y = ecdf_fun.ecdf(xa_low)

# Set up a figure with set of axes
fig, ax = plt.subplots(1, 1)

# Add axis labels
ax.set_xlabel('Cross-sectional area (µm$^2$)')
ax.set_ylabel('ECDF');

# Generate the histogram for the low-density fed mother
_ = ax.plot(x, y, marker='.', linestyle='none')

plt.show()
