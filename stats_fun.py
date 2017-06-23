import numpy as np
import matplotlib.pyplot as plt
import bootcamp_utils as bcu

import seaborn as sns
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})

bd_1975 = np.loadtxt('data/beak_depth_scandens_1975.csv')
bd_2012 = np.loadtxt('data/beak_depth_scandens_2012.csv')

def ecdf(data):
    """Generate x and y values for plotting an ECDF."""
    return np.sort(data), np.arange(1, len(data)+1) / len(data)

# Compute ECDFs for 1975 and 2012
x_1975, y_1975 = ecdf(bd_1975)
x_2012, y_2012 = ecdf(bd_2012)

n_reps = 100000

bs_reps = [bcu.bs_replicate(bd_2012, func=np.mean) for _ in range(n_reps)]
# # Plot the ECDFs
# fig, ax = plt.subplots(1, 1)
# ax.set_xlabel('beak depth (mm)')
# ax.set_ylabel('ECDF')
# _ = ax.plot(x_1975, y_1975, marker='.', linestyle='none')
# _ = ax.plot(x_2012, y_2012, marker='.', linestyle='none')
#
# ax.legend(('1975', '2012'), loc='upper right');
#
# plt.show()
